# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'swiim.ui'
#
# Created: Sat May 26 19:58:25 2012
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
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        swiimQMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(swiimQMainWindow)
        self.statusbar.setObjectName("statusbar")
        swiimQMainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(swiimQMainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName("toolBar")
        swiimQMainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew = QtGui.QAction(swiimQMainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../.designer/backup/images/wiimote.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionNew.setIcon(icon)
        self.actionNew.setIconVisibleInMenu(True)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(swiimQMainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionTest = QtGui.QAction(swiimQMainWindow)
        self.actionTest.setObjectName("actionTest")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionTest)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(swiimQMainWindow)
        QtCore.QMetaObject.connectSlotsByName(swiimQMainWindow)

    def retranslateUi(self, swiimQMainWindow):
        swiimQMainWindow.setWindowTitle(QtGui.QApplication.translate("swiimQMainWindow", "Swiim", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("swiimQMainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("swiimQMainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("swiimQMainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("swiimQMainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTest.setText(QtGui.QApplication.translate("swiimQMainWindow", "Test", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    swiimQMainWindow = QtGui.QMainWindow()
    ui = Ui_swiimQMainWindow()
    ui.setupUi(swiimQMainWindow)
    swiimQMainWindow.show()
    sys.exit(app.exec_())

