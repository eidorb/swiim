import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4'] = 'PySide'
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg

class MatplotlibWidget(FigureCanvasQTAgg):
    """Plots data using matplotlib.

    MatplotlibWidget subclasses FigureCanvasQTAgg, a valid QWidget and interface
    between matplotlib and PySide.

    plot exposes the figure's axes' plot function.

    """
    def __init__(self):
        self.figure = Figure()
        super(MatplotlibWidget, self).__init__(self.figure)
        self.axes = self.figure.add_subplot(1,1,1)

    def plot(self, *args, **kwargs):
        self.axes.plot(*args, **kwargs)

