import logging
import threading
from PySide import QtCore, QtGui
import operator
import wiiuse

logger = logging.getLogger('swiim.ui.states')

class Controller(QtCore.QObject):
    connect_succeeded = QtCore.Signal()
    connect_failed = QtCore.Signal()
    status_update = QtCore.Signal(dict)
    wiimote_disconnected = QtCore.Signal()

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
        # Connect other signals
        self.status_update.connect(self.update)
        self.button_map = {
            wiiuse.WIIMOTE_BUTTON_TWO: self.view.ui.btn2,
            wiiuse.WIIMOTE_BUTTON_ONE: self.view.ui.btn1,
            wiiuse.WIIMOTE_BUTTON_B: self.view.ui.btnB,
            wiiuse.WIIMOTE_BUTTON_A: self.view.ui.btnA,
            wiiuse.WIIMOTE_BUTTON_MINUS: self.view.ui.btnMinus,
            wiiuse.WIIMOTE_BUTTON_HOME: self.view.ui.btnHome,
            wiiuse.WIIMOTE_BUTTON_LEFT: self.view.ui.btnLeft,
            wiiuse.WIIMOTE_BUTTON_RIGHT: self.view.ui.btnRight,
            wiiuse.WIIMOTE_BUTTON_DOWN: self.view.ui.btnDown,
            wiiuse.WIIMOTE_BUTTON_UP: self.view.ui.btnUp,
            wiiuse.WIIMOTE_BUTTON_PLUS: self.view.ui.btnPlus,
        }
        self.led_control_map = {
            self.view.ui.controlLed1: wiiuse.WIIMOTE_LED_1,
            self.view.ui.controlLed2: wiiuse.WIIMOTE_LED_2,
            self.view.ui.controlLed3: wiiuse.WIIMOTE_LED_3,
            self.view.ui.controlLed4: wiiuse.WIIMOTE_LED_4,
        }
        self.led_map = {
            wiiuse.WIIMOTE_LED_1: self.view.ui.led1,
            wiiuse.WIIMOTE_LED_2: self.view.ui.led2,
            wiiuse.WIIMOTE_LED_3: self.view.ui.led3,
            wiiuse.WIIMOTE_LED_4: self.view.ui.led4,
        }
        # State machine
        self.state_machine = QtCore.QStateMachine()
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
        communication_state.addTransition(
            self.wiimote_disconnected, disconnected_state)

        self.state_machine.start()

    def disconnected_entered(self):
        logger.debug('Entered disconnected state')
        self.view.set_permanent_message('Disconnected from Wiimote')
        # Hide button highlights
        for control in self.button_map.itervalues():
            control.hide()
        # Hide LED lights
        for led_light in self.led_map.itervalues():
            led_light.hide()
        # Set battery level to 0
        self.view.ui.statusBattery.setValue(0)
        # Disable disconnect button
        self.view.ui.connect.setEnabled(True)
        self.view.ui.disconnect.setEnabled(False)
        # Disable Wiimote control
        self.view.ui.wiimote.setEnabled(False)

    def communication_entered(self):
        logger.debug('Entered communication state')
        # Disable connect button
        self.view.ui.connect.setEnabled(False)
        self.wiimote = wiiuse.Wiimote(self)

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
        self.wiimote.disconnected = True
        logger.debug('Waiting for poll thread to end')
        self.poll_thread.join()
        logger.debug('Poll thread ended')

    def set_leds(self):
        """Set the LEDs on the Wiimote according to the checkbox controls."""

        self.view.show_temporary_message('Setting LEDs')
        # Led controls that are checked
        leds = [led for control, led in self.led_control_map.iteritems()
                if control.isChecked()]
        # Bitwise OR the led codes
        led_state = reduce(operator.or_, leds, 0)
        self.wiimote.set_leds(led_state)

    def toggle_rumble(self):
        """Toggle the rumble on the Wiimote."""

        self.view.show_temporary_message('Toggling rumble')
        self.wiimote.toggle_rumble()

    @QtCore.Slot(list)
    def update(self, status):
        """Hide all the button highlights, then iterate through buttons and show
        the corresponding button highlights."""

        # Update button highlights
        for button_highlight in self.button_map.itervalues():
            button_highlight.hide()
        for button in status['buttons']:
            self.button_map[button].show()
        # Update LED lights
        for led_light in self.led_map.itervalues():
            led_light.hide()
        for led in status['leds']:
            self.led_map[led].show()
        # Update batery level
        self.view.ui.statusBattery.setValue(int(status['battery_level'] * 100))