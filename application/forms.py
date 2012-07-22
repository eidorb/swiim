from PySide import QtGui
from matplotlibwidget import MatplotlibWidget
from ui import swiim, wiimote_test
from wiiuse import wiiuse

class SwiimWindow(QtGui.QMainWindow, swiim.Ui_swiimQMainWindow):
    def __init__(self, parent=None):
        super(SwiimWindow, self).__init__(parent)
        self.setupUi(self)
        self.setup()

    def setup(self):
        self.permanent_message = QtGui.QLabel()
        self.statusbar.addPermanentWidget(self.permanent_message)

class WiimoteTestForm(QtGui.QWidget, wiimote_test.Ui_wiimoteTestQWidget):
    def __init__(self, parent=None):
        super(WiimoteTestForm, self).__init__(parent)
        self.setupUi(self)
        # Add plot widget
        self.plot = MatplotlibWidget(self.plotGroupBox)
        self.plotVerticalLayout.addWidget(self.plot)
        # Map from wiiuse button values to button highlight widgets
        self.button_highlights_map = {
            wiiuse.WIIMOTE_BUTTON_TWO: self.btn2,
            wiiuse.WIIMOTE_BUTTON_ONE: self.btn1,
            wiiuse.WIIMOTE_BUTTON_B: self.btnB,
            wiiuse.WIIMOTE_BUTTON_A: self.btnA,
            wiiuse.WIIMOTE_BUTTON_MINUS: self.btnMinus,
            wiiuse.WIIMOTE_BUTTON_HOME: self.btnHome,
            wiiuse.WIIMOTE_BUTTON_LEFT: self.btnLeft,
            wiiuse.WIIMOTE_BUTTON_RIGHT: self.btnRight,
            wiiuse.WIIMOTE_BUTTON_DOWN: self.btnDown,
            wiiuse.WIIMOTE_BUTTON_UP: self.btnUp,
            wiiuse.WIIMOTE_BUTTON_PLUS: self.btnPlus
        }
        # Map from wiiuse LED values to LED highlight widgets
        self.led_highlights_map = {
            wiiuse.WIIMOTE_LED_1: self.led1,
            wiiuse.WIIMOTE_LED_2: self.led2,
            wiiuse.WIIMOTE_LED_3: self.led3,
            wiiuse.WIIMOTE_LED_4: self.led4
        }
        # Map from LED control widgets to wiiuse button values
        self.led_controls_map = {
            self.controlLed1: wiiuse.WIIMOTE_LED_1,
            self.controlLed2: wiiuse.WIIMOTE_LED_2,
            self.controlLed3: wiiuse.WIIMOTE_LED_3,
            self.controlLed4: wiiuse.WIIMOTE_LED_4
        }
