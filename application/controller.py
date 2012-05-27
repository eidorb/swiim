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
        self.create_states()

    def create_states(self):
        """Create the states that make up the state machine."""
        self.initial = Initial(self, self)
        self.wiimote_test = WiimoteTest(self, self)

        self.initial.setup_transitions()

        self.setInitialState(self.initial)

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
        self.addTransition(
            self.app.forms['swiim'].actionTestWiimote.triggered,
            self.state_machine.wiimote_test)

    def onEntry(self, event):
        log.debug('Initial state entered')

class WiimoteTest(SwiimState):
    def onEntry(self, event):
        log.debug('Test Wiimote state entered')
        self.app.set_permanent_message('Wiimote connection test')
        wiimote_test = self.app.forms['wiimote_test']
        # Hide button highlights
        for highlight in wiimote_test.button_highlights_map.itervalues():
            highlight.hide()
        # Hide LED highlights
        for highlight in wiimote_test.led_highlights_map.itervalues():
            highlight.hide()
        # Set battery level to 0
        wiimote_test.statusBattery.setValue(0)
        # Disable disconnect button
        wiimote_test.connect.setEnabled(True)
        wiimote_test.disconnect.setEnabled(False)
        # Disable Wiimote control and status group boxes
        wiimote_test.controlGroup.setEnabled(False)
        wiimote_test.statusGroup.setEnabled(False)
        # Disable test wiimote action
        self.app.forms['swiim'].actionTestWiimote.setEnabled(False)
        # Set the test wiimote form as current stacked widget
        self.app.forms['swiim'].stackedWidget.setCurrentWidget(wiimote_test)

    def onExit(self, *args, **kwargs):
        # Re-enable test wiimote action
        self.app.forms['swiim'].actionTestWiimote.setEnabled(True)

class Disconnected(SwiimState):
    def onEntry(self, event):
        log.debug('Disconnected state entered')

    def onExit(self, event):
        log.debug('Disconnected state exited')