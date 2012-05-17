import logging
import sys
from PySide import QtGui
import os
from ui import wiimote
from ui.states import Controller

logger = logging.getLogger('swiim')

class View(object):
    def __init__(self):
        # Change dir for ui images
        os.chdir(os.path.dirname(wiimote.__file__))
        self.main_window = QtGui.QMainWindow()
        self.ui = wiimote.Ui_MainWindow()
        self.ui.setupUi(self.main_window)
        # Statusbar permanent message
        self._permanentMessage = QtGui.QLabel()
        self.ui.statusbar.addPermanentWidget(self._permanentMessage)
        self.main_window.show()

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

    app.exec_()
    logger.info('Program exiting')
    sys.exit()

if __name__ == '__main__':
    main()