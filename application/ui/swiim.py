# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'swiim.ui'
#
# Created: Sat May 26 22:29:50 2012
#      by: pyside-uic 0.2.13 running on PySide 1.0.7
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_swiimQMainWindow(object):
    def setupUi(self, swiimQMainWindow):
        swiimQMainWindow.setObjectName("swiimQMainWindow")
        swiimQMainWindow.resize(800, 600)
        swiimQMainWindow.setMinimumSize(QtCore.QSize(600, 600))
        self.centralwidget = QtGui.QWidget(swiimQMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        swiimQMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(swiimQMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.menu_Tools.addAction(self.actionTestWiimote)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Tools.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolBar.addAction(self.actionTestWiimote)

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


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    swiimQMainWindow = QtGui.QMainWindow()
    ui = Ui_swiimQMainWindow()
    ui.setupUi(swiimQMainWindow)
    swiimQMainWindow.show()
    sys.exit(app.exec_())

