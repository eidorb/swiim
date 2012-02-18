import logging
import threading
from PySide import QtCore, QtGui
from wiiuse import Wiimote

logger = logging.getLogger('swiim.ui.states')

class Controller(QtCore.QObject):
    connect_succeeded = QtCore.Signal()
    connect_failed = QtCore.Signal()

    def __init__(self, view):
        super(Controller, self).__init__()
        logger.debug('Initialising controller')
        self.view = view
        self.state_machine = QtCore.QStateMachine()
        # States
        disconnected_state = QtCore.QState(self.state_machine)
        communication_state = QtCore.QState(self.state_machine)
        connect_state = QtCore.QState(communication_state)
        connected_state = QtCore.QState(communication_state)
        self.state_machine.setInitialState(disconnected_state)
        communication_state.setInitialState(connect_state)

        disconnected_state.entered.connect(self.disconnected_entered)
        communication_state.entered.connect(self.communication_entered)
        connect_state.entered.connect(self.connect_entered)
        connected_state.entered.connect(self.connected_entered)
        connected_state.exited.connect(self.connected_exited)

        # Transitions
        disconnected_state.addTransition(
            view.ui.connect.clicked, communication_state)
        connect_state.addTransition(self.connect_succeeded, connected_state)
        connect_state.addTransition(self.connect_failed, disconnected_state)
        communication_state.addTransition(view.ui.disconnect.clicked, disconnected_state)

        self.state_machine.start()

    def disconnected_entered(self):
        logger.debug('Entered disconnected state')
        self.view.set_permanent_message('Disconnected from Wiimote')
        # Hide the button highlights initially
        for child in self.view.ui.wiimoteImageHolder.findChildren(QtGui.QLabel):
            child.hide()
        self.view.ui.wiimoteImage.show()
        # Disable disconnect button
        self.view.ui.connect.setEnabled(True)
        self.view.ui.disconnect.setEnabled(False)
        # Disable Wiimote control
        self.view.ui.wiimote.setEnabled(False)

    def communication_entered(self):
        logger.debug('Entered communication state')
        # Disable connect button
        self.view.ui.connect.setEnabled(False)
        self.wiimote = Wiimote()

    def connect_entered(self):
        logger.debug('Entered connect state')
        self.view.set_permanent_message('Connecting to Wiimote')
        if self.wiimote.connect():
            self.connect_succeeded.emit()
        else:
            self.connect_failed.emit()

    def connected_entered(self):
        logger.debug('Entered connected state')
        self.view.set_permanent_message('Connected to Wiimote')
        # Enable disconnect button
        self.view.ui.disconnect.setEnabled(True)
        # Enable Wiimote control
        self.view.ui.wiimote.setEnabled(True)

        self.poll_thread = threading.Thread(target=self.wiimote.poll)
        self.poll_thread.start()

    def connected_exited(self):
        self.wiimote.disconnect = True
        logger.debug('Waiting for poll thread to end')
        self.poll_thread.join()
        logger.debug('Poll thread ended')