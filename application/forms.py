from ui import swiim, wiimote_test
from PySide import QtGui

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