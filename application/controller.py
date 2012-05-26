from PySide import QtCore
import logging
from PySide.QtCore import QState
import view

log = logging.getLogger('swiim.' + __name__)

def start_application():
    log.info('Application starting')
    app = view.SwiimApplication()
    state_machine = StateMachine(app)
    log.debug('Starting state machine')
    state_machine.start()
    app.run()
    log.info('Application exiting')

class StateMachine(QtCore.QStateMachine):
    def __init__(self, app):
        super(StateMachine, self).__init__()
        self.app = app
        self.create_states()

    def create_states(self):
        """Create the states that make up the state machine."""

        self.initial = Initial(self)
        self.test_wiimote = TestWiimote(self)

        self.initial.setup_transitions()

        self.setInitialState(self.initial)

class Initial(QState):
    def setup_transitions(self):
        self.addTransition(
            self.machine().app.forms.swiim.actionTestWiimote.triggered,
            self.machine().test_wiimote)

    def onEntry(self, event):
        log.debug('Initial state entered')

class TestWiimote(QState):
    def onEntry(self, event):
        log.debug('Test state entered')
        self.machine().app.set_permanent_message('Wiimote connection test')
        # Disable test wiimote action
        self.machine().app.forms.swiim.actionTestWiimote.setEnabled(False)
        # Set the test wiimote form as the central widget
        self.machine().app.forms.swiim.setCentralWidget(
            self.machine().app.forms.wiimote_test
        )

    def onExit(self, *args, **kwargs):
        # Re-enable test wiimote action
        self.machine().app.forms.swiim.actionTestWiimote.setEnabled(True)


class Disconnected(QState):
    def onEntry(self, event):
        log.debug('Disconnected state entered')

    def onExit(self, event):
        log.debug('Disconnected state exited')