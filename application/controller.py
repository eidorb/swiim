from PySide import QtCore, QtGui
import logging
from PySide.QtCore import QState
import os
import view
from ui import test

log = logging.getLogger('swiim.' + __name__)

def start_application():
    log.info('Application starting')
    app = view.SwiimApplication()
    state_machine = StateMachine(app)
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
        self.test = Test(self)

        self.setInitialState(self.initial)

class Initial(QState):
    def onEntry(self, event):
        # Set up signals
        self.addTransition(self.machine().app.main_window.actionNew.triggered,
                           self.machine().test)
        self.machine().app.set_permanent_message(
            'Select New from the File menu to test'
        )

class Test(QState):
    def onEntry(self, event):
        log.debug('Test state entered')
        self.machine().app.set_permanent_message('Testing')
        # Change directory for correct referencing of image files
        os.chdir(os.path.join(os.path.dirname(__file__), 'ui'))

        test_form = test.Ui_Form()
        test_form.widget = QtGui.QWidget()
        test_form.setupUi(test_form.widget)
        self.machine().app.main_window.widget.setCentralWidget(test_form.widget)

class Disconnected(QState):
    def onEntry(self, event):
        log.debug('Disconnected state entered')
        self.machine().app.set_permanent_message('Disconnected')

    def onExit(event):
        log.debug('Disconnected state exited')