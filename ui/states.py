import logging
import threading
from PySide import QtCore, QtGui
import operator
import _wiiuse
from wiiuse import Wiimote

logger = logging.getLogger('swiim.ui.states')

class Controller(QtCore.QObject):
    connect_succeeded = QtCore.Signal()
    connect_failed = QtCore.Signal()

    def __init__(self, view):
        super(Controller, self).__init__()
        logger.debug('Initialising controller')
        self.view = view
        # Connect controls
        self.view.ui.controlRumble.clicked.connect(self.toggle_rumble)
        self.view.ui.controlLed1.clicked.connect(self.set_leds)
        self.view.ui.controlLed2.clicked.connect(self.set_leds)
        self.view.ui.controlLed3.clicked.connect(self.set_leds)
        self.view.ui.controlLed4.clicked.connect(self.set_leds)
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
        communication_state.addTransition(
            view.ui.disconnect.clicked, disconnected_state)

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

    def set_leds(self):
        self.view.show_temporary_message('Setting LEDs')
        led_map = {
            'controlLed1': _wiiuse.WIIMOTE_LED_1,
            'controlLed2': _wiiuse.WIIMOTE_LED_2,
            'controlLed3': _wiiuse.WIIMOTE_LED_3,
            'controlLed4': _wiiuse.WIIMOTE_LED_4}
        # Assess which of the LED controls are checked. Bitwise OR the
        # the corresponding LED values.
        is_control_checked = lambda control: getattr(self.view.ui, control).isChecked()
        leds = [led for control, led in led_map.iteritems()
                if is_control_checked(control)]
        led_state = reduce(operator.or_, leds, 0)
        self.wiimote.set_leds(led_state)

    def toggle_rumble(self):
        self.view.show_temporary_message('Toggling rumble')
        self.wiimote.toggle_rumble()