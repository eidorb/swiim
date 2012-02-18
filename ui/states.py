import logging
from PySide import QtCore, QtGui
from wiiuse import Wiimote

logger = logging.getLogger('swiim.ui.states')

class Controller(object):
    def __init__(self, view):
        logger.debug('Initialising controller')
        self.view = view
        self.state_machine = QtCore.QStateMachine()
        # States
        disconnected_state = QtCore.QState(self.state_machine)
        disconnected_state.entered.connect(self.disconnected_entered)

        communication_state = QtCore.QState(self.state_machine)
        communication_state.entered.connect(self.communication_entered)

        connect_state = QtCore.QState(communication_state)
        connect_state.entered.connect(self.connect_entered)

        connected_state = QtCore.QState(communication_state)
        connected_state.entered.connect(self.connected_entered)

        self.state_machine.setInitialState(disconnected_state)
        communication_state.setInitialState(connect_state)

        # Transitions
        disconnected_state.addTransition(
            view.ui.connect.clicked, communication_state)

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

    def connect_entered(self):
        logger.debug('Entered connect state')
        self.view.set_permanent_message('Connecting to Wiimote')
        self.wiimote = Wiimote()
        logger.error('%s', wiimote.BUTTON_A)

    def connected_entered(self):
        logger.debug('Entered connected state')
        self.view.set_permanent_message('Connected to Wiimote')
        # Enable disconnect button
        self.view.ui.disconnect.setEnabled(True)
        # Enable Wiimote control
        self.view.ui.wiimote.setEnabled(True)