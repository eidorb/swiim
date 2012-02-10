import logging
import sys
from PySide import QtGui, QtCore
import operator
import os
from ui import wiimote
from wiiuse import Wiimote

logger = logging.getLogger('swiim')

class WiimoteWindow(object):
    def __init__(self):
        # Change dir for ui images
        os.chdir(os.path.dirname(wiimote.__file__))
        self.main_window = QtGui.QMainWindow()
        self.ui = wiimote.Ui_MainWindow()
        self.ui.setupUi(self.main_window)
        # Hide the button highlights initially
        for child in self.ui.wiimoteImageHolder.findChildren(QtGui.QLabel):
            child.hide()
        self.ui.wiimoteImage.show()
        # Connect controls
        self.ui.controlRumble.clicked.connect(self._toggle_rumble)
        self.ui.controlLed1.clicked.connect(self._set_leds)
        self.ui.controlLed2.clicked.connect(self._set_leds)
        self.ui.controlLed3.clicked.connect(self._set_leds)
        self.ui.controlLed4.clicked.connect(self._set_leds)
        # Statusbar permanent message
        self._permanentMessage = QtGui.QLabel()
        self.ui.statusbar.addPermanentWidget(self._permanentMessage)
        self.main_window.show()

    # Control slot
    def _toggle_rumble(self):
        self.show_temporary_message('Toggling rumble')
        logger.debug('Toggling rumble')

    # Control slot
    def _set_leds(self):
        self.show_temporary_message('Setting LEDs')
        led_map = {
            'controlLed1': Wiimote.LED_1,
            'controlLed2': Wiimote.LED_2,
            'controlLed3': Wiimote.LED_3,
            'controlLed4': Wiimote.LED_4,
        }
        # Assess which of the LED controls are checked. Bitwise or the
        # the corresponding LED values.
        is_control_checked = lambda control: getattr(self.ui, control).isChecked()
        leds = [led for control, led in led_map.iteritems() if is_control_checked(control)]
        led_state = reduce(operator.or_, leds, 0)
        logger.debug('Setting LED state to {:08b}'.format(led_state))

    # Status slot
    def _update_status(self):
        # TODO: Given the status of the wiimote, show pressed button images,
        #       show lit LEDs and update battery life progress bar.
        pass

    def set_permanent_message(self, message):
        self._permanentMessage.setText(message)

    def show_temporary_message(self, message):
        self.ui.statusbar.showMessage(message, 600)

    class WiiuseThread(QtCore.QThread):
        def run(self):
            pass
            

def main():
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(name)s %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)



    app = QtGui.QApplication(sys.argv)
    wiimote_window = WiimoteWindow()

#    # State machine
#    state_machine = QtCore.QStateMachine()
#    disconnected = QtCore.QState(state_machine)
#    def disconnected_entered():
#        # TODO: State statusbar messages
#        wiimote_window.set_permanent_message('Disconnected from wiimote')
#
#    disconnected.entered.connect(disconnected_entered)
#
#    attempt_connection = QtCore.QState()
#    connected = QtCore.QState()
#    diagnostics = QtCore.QState()
#
#    state_machine.setInitialState(disconnected)
#    state_machine.start()

    state_machine = QtCore.QStateMachine()
    disconnected_state = DisconnectedState(wiimote_window, state_machine)
    connected_state = ConnectedState(wiimote_window, state_machine)

    disconnected_state.addTransition(
        wiimote_window.ui.connect.clicked, connected_state)

    state_machine.setInitialState(disconnected_state)
    state_machine.start()



    sys.exit(app.exec_())

class DisconnectedState(QtCore.QState):
    def __init__(self, wiimote_window, *args, **kwargs):
        super(DisconnectedState, self).__init__(*args, **kwargs)
        self.wiimote_window = wiimote_window


    def onEntry(self, *args, **kwargs):
        """"""
        # Wiimote interaction disabled until connected
        logger.debug('Entered disconnected state')
        self.wiimote_window.set_permanent_message('Disconnected from wiimote')
        self.wiimote_window.ui.wiimote.setEnabled(False)
        self.wiimote_window.ui.connect.setEnabled(True)
        self.wiimote_window.ui.disconnect.setEnabled(False)

class ConnectedState(QtCore.QState):
    def __init__(self, wiimote_window, *args, **kwargs):
        super(ConnectedState, self).__init__(*args, **kwargs)
        self.wiimote_window = wiimote_window

    def onEntry(self, *args, **kwargs):
        """"""
        logger.debug('Entered connected state')
        # Enable Wiimote interaction
        self.wiimote_window.ui.connect.setEnabled(False)

class myState(QtCore.QState):
    def onEntry(self, *args, **kwargs):
        print 'hi'

if __name__ == '__main__':
    main()