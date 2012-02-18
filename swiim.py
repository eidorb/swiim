import logging
import sys
from PySide import QtGui
import operator
import os
from ui import wiimote, states
from ui.states import Controller
from wiiuse import Wiimote

logger = logging.getLogger('swiim')

class View(object):
    def __init__(self):
        # Change dir for ui images
        os.chdir(os.path.dirname(wiimote.__file__))
        self.main_window = QtGui.QMainWindow()
        self.ui = wiimote.Ui_MainWindow()
        self.ui.setupUi(self.main_window)
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

def main():
    # Setup logging
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(name)s %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # Create a Qt app and create populate the main window with a form
    app = QtGui.QApplication(sys.argv)
    view = View()

    controller = Controller(view)

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()