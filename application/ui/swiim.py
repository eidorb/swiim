from PySide import QtCore, QtGui

class Ui_swiimQMainWindow(object):
    def setupUi(self, swiimQMainWindow):
        swiimQMainWindow.setObjectName("swiimQMainWindow")
        swiimQMainWindow.resize(800, 600)
        swiimQMainWindow.setMinimumSize(QtCore.QSize(600, 600))
        self.centralwidget = QtGui.QWidget(swiimQMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.horizontalLayout.addWidget(self.stackedWidget)
        swiimQMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menu_Tools = QtGui.QMenu(self.menubar)
        self.menu_Tools.setObjectName("menu_Tools")
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        swiimQMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(swiimQMainWindow)
        self.statusbar.setObjectName("statusbar")
        swiimQMainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(swiimQMainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName("toolBar")
        swiimQMainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionTestWiimote = QtGui.QAction(swiimQMainWindow)
        self.actionTestWiimote.setObjectName("actionTestWiimote")
        self.actionHome = QtGui.QAction(swiimQMainWindow)
        self.actionHome.setObjectName("actionHome")
        self.menu_Tools.addAction(self.actionTestWiimote)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Tools.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolBar.addAction(self.actionTestWiimote)
        self.toolBar.addAction(self.actionHome)

        self.retranslateUi(swiimQMainWindow)
        QtCore.QMetaObject.connectSlotsByName(swiimQMainWindow)

    def retranslateUi(self, swiimQMainWindow):
        swiimQMainWindow.setWindowTitle(QtGui.QApplication.translate("swiimQMainWindow", "Swiim", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Tools.setTitle(QtGui.QApplication.translate("swiimQMainWindow", "&Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("swiimQMainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("swiimQMainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("swiimQMainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTestWiimote.setText(QtGui.QApplication.translate("swiimQMainWindow", "Test &Wiimote", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTestWiimote.setToolTip(QtGui.QApplication.translate("swiimQMainWindow", "Test connection with the Wiimote", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHome.setText(QtGui.QApplication.translate("swiimQMainWindow", "&Home", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHome.setToolTip(QtGui.QApplication.translate("swiimQMainWindow", "Go to the home screen", None, QtGui.QApplication.UnicodeUTF8))

