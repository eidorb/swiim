import logging
from PySide import QtCore

logger = logging.getLogger('swiim.ui.states')

class WiimoteWindowState(QtCore.QState):
    """This state contains a reference to the Wiimote window Qt object"""

    def __init__(self, *args, **kwargs):
        super(WiimoteWindowState, self).__init__(*args, **kwargs)
        self.wiimote_window = WiimoteWindowState.wiimote_window

class DisconnectedState(WiimoteWindowState):
    def onEntry(self, *args, **kwargs):
        logger.debug('Entered disconnected state')
        self.wiimote_window.set_permanent_message('Disconnected from Wiimote')
        # Disable disconnect button
        self.wiimote_window.ui.connect.setEnabled(True)
        self.wiimote_window.ui.disconnect.setEnabled(False)
        # Disable Wiimote control
        self.wiimote_window.ui.wiimote.setEnabled(False)

class CommunicationState(WiimoteWindowState):
    def onEntry(self, *args, **kwargs):
        logger.debug('Entered communication state')
        # Disable connect button
        self.wiimote_window.ui.connect.setEnabled(False)

class ConnectState(WiimoteWindowState):
    def onEntry(self, *args, **kwargs):
        logger.debug('Entered connect state')
        self.wiimote_window.set_permanent_message('Connecting to Wiimote')

class ConnectedState(WiimoteWindowState):
    def onEntry(self, *args, **kwargs):
        logger.debug('Entered connected state')
        self.wiimote_window.set_permanent_message('Connected to Wiimote')
        # Enable disconnect button
        self.wiimote_window.ui.disconnect.setEnabled(True)
        # Enable Wiimote control
        self.wiimote_window.ui.wiimote.setEnabled(True)

def create_state_machine(wiimote_window):
    logger.debug('Setting up state machine')
    WiimoteWindowState.wiimote_window = wiimote_window
    state_machine = QtCore.QStateMachine()
    # States
    disconnected_state = DisconnectedState(state_machine)
    communication_state = CommunicationState(state_machine)
    connect_state = ConnectState(communication_state)
    connected_state = ConnectedState(communication_state)
    state_machine.setInitialState(disconnected_state)
    communication_state.setInitialState(connect_state)
    # Transitions
    disconnected_state.addTransition(
        wiimote_window.ui.connect.clicked, communication_state)
    return state_machine
