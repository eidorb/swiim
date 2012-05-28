from PySide import QtCore
import logging
from PySide.QtCore import QState
import view

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

class SwiimState(QState):
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
        self.addTransition(self.app.forms['swiim'].actionTestWiimote.triggered,
                           self.state_machine.states['wiimote_test'])

    def onEntry(self, event):
        log.debug('Initial state entered')
        self.app.set_permanent_message('Home')
        # Show the home form
        self.app.forms['swiim'].stackedWidget.setCurrentWidget(
            self.app.forms['home'])

class WiimoteTest(SwiimState):
    def __init__(self, parent, state_machine):
        """Perform custom initialisation for the wiimote test state.

        This state has two substates: disconnected and disconnected. These
        states are created with this state as the parent. The disconnected state
        is set as this state's initial state.

        """
        super(WiimoteTest, self).__init__(parent, state_machine)
        state_machine.states.update(
            wiimote_test_disconnected=WiimoteTestDisconnected(self, state_machine),
            wiimote_test_connected=WiimoteTestConnected(self, state_machine)
        )
        self.setInitialState(state_machine.states['wiimote_test_disconnected'])

    def setup_transitions(self):
        """Add wiimote test state transitions.

        To initial state
            when home action triggered.
        """

        self.addTransition(self.app.forms['swiim'].actionHome.triggered,
                           self.state_machine.states['initial'])

    def onEntry(self, event):
        log.debug('Test Wiimote state entered')
        wiimote_test = self.app.forms['wiimote_test']
        # Disable test wiimote action
        self.app.forms['swiim'].actionTestWiimote.setEnabled(False)
        # Disable the connection controls
        wiimote_test.connect.setEnabled(False)
        wiimote_test.disconnect.setEnabled(False)
        # Set the test wiimote form as current stacked widget
        self.app.forms['swiim'].stackedWidget.setCurrentWidget(wiimote_test)

    def onExit(self, *args, **kwargs):
        # Re-enable test wiimote action
        self.app.forms['swiim'].actionTestWiimote.setEnabled(True)

class WiimoteTestDisconnected(SwiimState):
    def onEntry(self, event):
        """Set up the wiimote test form for the disconnected state.

        Hide all the wiimote image overlays indicating status. Enable the
        connect button. Disable the control and status group.
        """
        log.debug('Wiimote test disconnected state entered')
        self.app.set_permanent_message(
            'Wiimote connection test: disconnected from wiimote')
        wiimote_test = self.app.forms['wiimote_test']
        # Hide button highlights
        for highlight in wiimote_test.button_highlights_map.itervalues():
            highlight.hide()
        # Hide LED highlights
        for highlight in wiimote_test.led_highlights_map.itervalues():
            highlight.hide()
        # Set battery level to 0
        wiimote_test.statusBattery.setValue(0)
        # Enable connect button
        wiimote_test.connect.setEnabled(True)
        # Disable Wiimote control and status group boxes
        wiimote_test.controlGroup.setEnabled(False)
        wiimote_test.statusGroup.setEnabled(False)

    def onExit(self, event):
        log.debug('Wiimote test disconnected state exited')
        # Disable the connect button
        self.app.forms['wiimote_test'].connect.setEnabled(False)

class WiimoteTestConnected(SwiimState):
    def onEntry(self, event):
        log.debug('Wiimote test connected state entered')
        self.app.set_permanent_message(
            'Wiimote connection test: connected to wiimote')
        wiimote_test = self.app.forms['wiimote_test']
        # Enable connect button
        wiimote_test.connect.setEnabled(True)

    def onExit(self, event):
        log.debug('Wiimote test connected state exited')
        # Disable the disconnect button
        self.app.forms['wiimote_test'].disconnect.setEnabled(False)