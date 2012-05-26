# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'swiim.ui'
#
# Created: Sat May 26 19:26:53 2012
#      by: pyside-uic 0.2.13 running on PySide 1.0.7
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Swiim(object):
    def setupUi(self, Swiim):
        Swiim.setObjectName("Swiim")
        Swiim.resize(800, 600)
        Swiim.setMinimumSize(QtCore.QSize(600, 600))
        self.centralwidget = QtGui.QWidget(Swiim)
        self.centralwidget.setObjectName("centralwidget")
        Swiim.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Swiim)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        Swiim.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Swiim)
        self.statusbar.setObjectName("statusbar")
        Swiim.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(Swiim)
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName("toolBar")
        Swiim.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew = QtGui.QAction(Swiim)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../.designer/backup/images/wiimote.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionNew.setIcon(icon)
        self.actionNew.setIconVisibleInMenu(True)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(Swiim)
        self.actionOpen.setObjectName("actionOpen")
        self.actionTest = QtGui.QAction(Swiim)
        self.actionTest.setObjectName("actionTest")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionTest)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(Swiim)
        QtCore.QMetaObject.connectSlotsByName(Swiim)

    def retranslateUi(self, Swiim):
        Swiim.setWindowTitle(QtGui.QApplication.translate("Swiim", "Swiim", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("Swiim", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("Swiim", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("Swiim", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("Swiim", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTest.setText(QtGui.QApplication.translate("Swiim", "Test", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Swiim = QtGui.QMainWindow()
    ui = Ui_Swiim()
    ui.setupUi(Swiim)
    Swiim.show()
    sys.exit(app.exec_())

