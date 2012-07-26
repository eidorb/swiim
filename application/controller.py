import logging
from PySide import QtCore
import view
from wiiuse import wiiuse

log = logging.getLogger('swiim.' + __name__)

def start_application():
    log.info('Application starting')
    app = view.SwiimApplication()
    state_machine = SwiimStateMachine(app)
    log.debug('Starting state machine')
    state_machine.start()
    app.run()
    log.info('Application exiting')

class SwiimStateMachine(QtCore.QStateMachine):
    """Sets up a reference to the app for convenience."""
    def __init__(self, app):
        super(SwiimStateMachine, self).__init__()
        self.app = app
        self.states = {}
        self.create_states()
        self.setInitialState(self.states['initial'])

    def create_states(self):
        """Create the states that make up the state machine."""
        self.states.update(
            initial=Initial(self, self),
            wiimote_test=WiimoteTest(self, self)
        )
        for state in self.states.itervalues():
            state.setup_transitions()

class SwiimState(QtCore.QState):
    """Sets up references to the state machine and app for convenience."""
    def __init__(self, parent, state_machine):
        super(SwiimState, self).__init__(parent)
        self.state_machine = state_machine
        self.app = state_machine.app

    def setup_transitions(self):
        pass

class Initial(SwiimState):
    def setup_transitions(self):
        """Add initial state transitions.

        To wiimote test state
            when wiimote test action triggered.

        """
        self.addTransition(self.app.forms['swiim'].testWiimoteAction.triggered,
                           self.state_machine.states['wiimote_test'])

    def onEntry(self, event):
        log.debug('Initial state entered')
        self.app.display_permanent_message('Home')
        # Show the home form
        self.app.forms['swiim'].stackedWidget.setCurrentWidget(
            self.app.forms['home'])

    def onExit(self, event):
        log.debug('Initial state exited')

class WiimoteTest(SwiimState):
    def __init__(self, parent, state_machine):
        """Perform custom initialisation for the wiimote test state.

        This state has two substates: disconnected and disconnected. These
        states are created with this state as the parent. The disconnected state
        is set as this state's initial state.

        """
        super(WiimoteTest, self).__init__(parent, state_machine)
        state_machine.states.update(
            wiimote_test_disconnected=WiimoteTestDisconnected(
                self, state_machine),
            wiimote_test_connected=WiimoteTestConnected(
                self, state_machine))
        self.setInitialState(state_machine.states['wiimote_test_disconnected'])
        self.app.forms['wiimote_test'].connectButton.clicked.connect(
            self.state_machine
                .states['wiimote_test_disconnected'].attempt_connection)

    def setup_transitions(self):
        """Add wiimote test state transitions.

        To initial state
            when home action triggered.

        """
        self.addTransition(self.app.forms['swiim'].homeAction.triggered,
                           self.state_machine.states['initial'])

    def onEntry(self, event):
        log.debug('Wiimote test state entered')
        wiimote_test = self.app.forms['wiimote_test']
        # Disable test wiimote action
        self.app.forms['swiim'].testWiimoteAction.setEnabled(False)
        # Disable the connection controls
        wiimote_test.connectButton.setEnabled(False)
        wiimote_test.disconnectButton.setEnabled(False)
        # Set the wiimote test form as current stacked widget
        self.app.forms['swiim'].stackedWidget.setCurrentWidget(wiimote_test)

    def onExit(self, event):
        log.debug('Wiimote test state exited')
        # Re-enable test wiimote action
        self.app.forms['swiim'].testWiimoteAction.setEnabled(True)

class WiimoteTestDisconnected(SwiimState):
    connection_attempt_successful = QtCore.Signal()
    connection_attempt_unsuccessful = QtCore.Signal()

    def setup_transitions(self):
        """Add wiimote test disconnected state transitions.

        To wiimote test connected state
            when connection attempt successful.
        Self transition
            when connection attempt unsuccessful.

        """
        self.addTransition(self.connection_attempt_successful,
                           self.state_machine.states['wiimote_test_connected'])
        self.addTransition(self.connection_attempt_unsuccessful,
                           self)

    def onEntry(self, event):
        """Set up the wiimote test form for the disconnected state.

        Hide all the wiimote image overlays indicating status. Enable the
        connect button. Disable the control and status group.

        """
        log.debug('Wiimote test disconnected state entered')
        self.app.display_permanent_message('Wiimote test: disconnected')
        wiimote_test = self.app.forms['wiimote_test']
        # Hide button highlights
        for highlight in wiimote_test.button_highlights_map.itervalues():
            highlight.hide()
        # Hide LED highlights
        for highlight in wiimote_test.led_highlights_map.itervalues():
            highlight.hide()
        # Set battery level to 0
        wiimote_test.batteryProgressBar.setValue(0)
        # Enable connect button
        wiimote_test.connectButton.setEnabled(True)
        # Disable Wiimote control, status and plot group boxes
        wiimote_test.controlGroupBox.setEnabled(False)
        wiimote_test.statusGroupBox.setEnabled(False)
        wiimote_test.plotGroupBox.setEnabled(False)

    def onExit(self, event):
        log.debug('Wiimote test disconnected state exited')
        # Disable the connect button
        self.app.forms['wiimote_test'].connectButton.setEnabled(False)

    def attempt_connection(self):
        """Attempt to establish a connection to a wiimote."""
        log.debug('Attempting connection')
        self.app.display_temporary_message('Attempting connection')
        # Disable the connect button while attempting connection.
        self.app.forms['wiimote_test'].connectButton.setEnabled(False)

        self.app.wiimote_connection = wiiuse.WiimoteConnection()
        if self.app.wiimote_connection.connect():
            # Connection attempt successful
            log.debug('Connection attempt successful')
            self.app.display_temporary_message('Connection attempt successful')
            self.connection_attempt_successful.emit()
        else:
            # Connection attempt unsuccessful
            log.debug('Connection attempt unsuccessful')
            self.app.display_temporary_message('Connection attempt unsuccessful')
            self.connection_attempt_unsuccessful.emit()

class WiimoteTestConnected(SwiimState):
    def setup_transitions(self):
        """
        Add wiimote test connected state transitions.

        To wiimote test disconnected state
            when disconnect button pressed or on connection error.

        """
        self.addTransition(
            self.app.forms['wiimote_test'].disconnectButton.clicked,
            self.state_machine.states['wiimote_test_disconnected'])

    def onEntry(self, event):
        log.debug('Wiimote test connected state entered')
        self.app.display_permanent_message('Wiimote test: connected')
        wiimote_test = self.app.forms['wiimote_test']
        # Enable disconnect button
        wiimote_test.disconnectButton.setEnabled(True)
        # Enable Wiimote control, status and plot group boxes
        wiimote_test.controlGroupBox.setEnabled(True)
        wiimote_test.statusGroupBox.setEnabled(True)
        wiimote_test.plotGroupBox.setEnabled(True)

    def onExit(self, event):
        log.debug('Wiimote test connected state exited')
        # Disable the disconnect button
        self.app.forms['wiimote_test'].disconnectButton.setEnabled(False)
