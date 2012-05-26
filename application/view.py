import logging
from PySide import QtGui
from ui import swiim

log = logging.getLogger('swiim.' + __name__)

class SwiimApplication(object):
    def __init__(self):
        self.application = QtGui.QApplication([])
        self.setup_ui()

    def setup_ui(self):
        """Create a main window. Populate with the swiim ui and display it"""

        class MainWindowForm(QtGui.QMainWindow, swiim.Ui_MainWindow):
            pass
        self.main_window = MainWindowForm()
        self.main_window.setupUi(self.main_window)
        # Add widget to status bar for permanent messages
        self.main_window.permanent_message = QtGui.QLabel()
        self.main_window.statusbar.addPermanentWidget(
            self.main_window.permanent_message)
        self.main_window.show()
        log.debug('Set up main UI')

    def set_permanent_message(self, message):
        """Set the permanent status bar message to `message`"""

        self.main_window.permanent_message.setText(message)

    def show_temporary_message(self, message):
        """Show `message` in the status bar temporarily"""

        self.main_window.statusbar.showMessage(message, 1000)

    def run(self):
        """Enter the qapplication's main event loop."""

        log.debug('Entering QApplication main loop')
        self.application.exec_()
        log.debug('Exited QApplication main loop')

class View(object):
    def __init__(self):
        # Change dir for ui images
        os.chdir(os.path.dirname(__file__))
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


