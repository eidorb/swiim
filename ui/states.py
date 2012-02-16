import logging
from PySide import QtCore


logger = logging.getLogger('swiim.ui.states')

class WiimoteWindowState(QtCore.QState):
    """This state contains a reference to the Wiimote window Qt object"""

    def __init__(self, wiimote_window, *args, **kwargs):
        super(WiimoteWindowState, self).__init__(*args, **kwargs)
        self.wiimote_window = wiimote_window

class DisconnectedState(WiimoteWindowState):
    def onEntry(self, *args, **kwargs):
        logger.debug('Entered disconnected state')
        self.wiimote_window.set_permanent_message('Disconnected from Wiimote')

        # Wiimote connection buttons
        self.wiimote_window.ui.connect.setEnabled(True)
        self.wiimote_window.ui.disconnect.setEnabled(False)

        # Wiimote control disabled while disconnected
        self.wiimote_window.ui.wiimote.setEnabled(False)

class CommunicationState(WiimoteWindowState):
    def onEntry(self, *args, **kwargs):
        logger.debug('Entered communication state')

        # Wiimote connection buttons
        self.wiimote_window.ui.connect.setEnabled(False)

def create_state_machine(wiimote_window):
    logger.debug('Setting up state machine')
    state_machine = QtCore.QStateMachine()
    # States
    disconnected_state = DisconnectedState(wiimote_window, state_machine)
    communication_state = CommunicationState(wiimote_window, state_machine)
    state_machine.setInitialState(disconnected_state)
    # Transitions
    disconnected_state.addTransition(
        wiimote_window.ui.connect.clicked, communication_state)
    return state_machine
