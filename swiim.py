import logging
import sys
from PySide import QtGui
import os
from ui import wiimote
from ui.states import Controller
import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PySide'
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

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
        # Add matplotlib widget
        # generate the plot
        fig = Figure(figsize=(600,600), dpi=72, facecolor=(1,1,1), edgecolor=(0,0,0))
        ax = fig.add_subplot(111)
        ax.plot([0,1])
        # generate the canvas to display the plot
        canvas = FigureCanvas(fig)

        # add the plot canvas to a window
        self.ui.connection.layout().addWidget(canvas)
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
    setup_logging()
    # Create a Qt app and create populate the main window with a form
    app = QtGui.QApplication(sys.argv)
    view = View()

    controller = Controller(view)

    app.exec_()
    logger.info('Program exiting')
    sys.exit()

def setup_logging():
    """Set up logging. Uses a StreamHandler to log to the console"""
    formatter = logging.Formatter('%(name)s %(levelname)s - %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)

if __name__ == '__main__':
    main()