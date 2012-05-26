import test
import swiim
from PySide import QtGui

class MainWindow(QtGui.QMainWindow, swiim.Ui_MainWindow):
    def __init__(self, parent):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

class TestForm(QtGui.QWidget, test.Ui_Form):
    def __init__(self, parent):
        super(TestForm, self).__init__(parent)
        self.setupUi(self)