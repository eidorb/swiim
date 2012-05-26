import logging
from PySide import QtGui
import os
from forms import SwiimWindow, WiimoteTestForm

log = logging.getLogger('swiim.' + __name__)

class SwiimApplication(object):
    def __init__(self):
        self.application = QtGui.QApplication([])
        self.setup_forms()

    class forms(object):
        pass

    def setup_forms(self):
        """Load the form classes and display the main window."""

        log.debug('Loading forms')
        # Change directory for correct referencing of image files
        os.chdir(os.path.join(os.path.dirname(__file__), 'ui'))
        self.forms.swiim = SwiimWindow()
        self.forms.wiimote_test = WiimoteTestForm()
        log.debug('Showing swiim window')
        self.forms.swiim.show()

    def set_permanent_message(self, message):
        """Set the permanent status bar message to `message`"""

        self.forms.swiim.permanent_message.setText(message)

    def show_temporary_message(self, message):
        """Show `message` in the status bar temporarily"""

        self.forms.swiim.statusbar.showMessage(message, 1000)

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


