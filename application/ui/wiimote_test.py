from PySide import QtCore, QtGui

class Ui_wiimoteTestQWidget(object):
    def setupUi(self, wiimoteTestQWidget):
        wiimoteTestQWidget.setObjectName("wiimoteTestQWidget")
        wiimoteTestQWidget.resize(773, 539)
        self.horizontalLayout_4 = QtGui.QHBoxLayout(wiimoteTestQWidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.leftVerticalLayout = QtGui.QVBoxLayout()
        self.leftVerticalLayout.setObjectName("leftVerticalLayout")
        self.connectionGroupBox = QtGui.QGroupBox(wiimoteTestQWidget)
        self.connectionGroupBox.setObjectName("connectionGroupBox")
        self.horizontalLayout = QtGui.QHBoxLayout(self.connectionGroupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.connectButton = QtGui.QPushButton(self.connectionGroupBox)
        self.connectButton.setObjectName("connectButton")
        self.horizontalLayout.addWidget(self.connectButton)
        self.disconnectButton = QtGui.QPushButton(self.connectionGroupBox)
        self.disconnectButton.setObjectName("disconnectButton")
        self.horizontalLayout.addWidget(self.disconnectButton)
        self.leftVerticalLayout.addWidget(self.connectionGroupBox)
        self.controlGroupBox = QtGui.QGroupBox(wiimoteTestQWidget)
        self.controlGroupBox.setEnabled(True)
        self.controlGroupBox.setObjectName("controlGroupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.controlGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toggleRumbleButton = QtGui.QPushButton(self.controlGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleRumbleButton.sizePolicy().hasHeightForWidth())
        self.toggleRumbleButton.setSizePolicy(sizePolicy)
        self.toggleRumbleButton.setText("Toggle Rumble")
        self.toggleRumbleButton.setObjectName("toggleRumbleButton")
        self.verticalLayout.addWidget(self.toggleRumbleButton)
        self.label_2 = QtGui.QLabel(self.controlGroupBox)
        self.label_2.setText("Set LEDs")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self._2 = QtGui.QHBoxLayout()
        self._2.setObjectName("_2")
        self.led1Button = QtGui.QCheckBox(self.controlGroupBox)
        self.led1Button.setText("")
        self.led1Button.setChecked(False)
        self.led1Button.setObjectName("led1Button")
        self._2.addWidget(self.led1Button)
        self.led2Button = QtGui.QCheckBox(self.controlGroupBox)
        self.led2Button.setText("")
        self.led2Button.setObjectName("led2Button")
        self._2.addWidget(self.led2Button)
        self.led3Button = QtGui.QCheckBox(self.controlGroupBox)
        self.led3Button.setText("")
        self.led3Button.setObjectName("led3Button")
        self._2.addWidget(self.led3Button)
        self.led4Button = QtGui.QCheckBox(self.controlGroupBox)
        self.led4Button.setText("")
        self.led4Button.setObjectName("led4Button")
        self._2.addWidget(self.led4Button)
        spacerItem = QtGui.QSpacerItem(79, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self._2.addItem(spacerItem)
        self.verticalLayout.addLayout(self._2)
        self.leftVerticalLayout.addWidget(self.controlGroupBox)
        spacerItem1 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.leftVerticalLayout.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.leftVerticalLayout)
        self.centreVerticalLayout = QtGui.QVBoxLayout()
        self.centreVerticalLayout.setObjectName("centreVerticalLayout")
        self.statusGroupBox = QtGui.QGroupBox(wiimoteTestQWidget)
        self.statusGroupBox.setObjectName("statusGroupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.statusGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.wiimoteImageContainer = QtGui.QWidget(self.statusGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wiimoteImageContainer.sizePolicy().hasHeightForWidth())
        self.wiimoteImageContainer.setSizePolicy(sizePolicy)
        self.wiimoteImageContainer.setMinimumSize(QtCore.QSize(157, 400))
        self.wiimoteImageContainer.setMaximumSize(QtCore.QSize(157, 400))
        self.wiimoteImageContainer.setObjectName("wiimoteImageContainer")
        self.wiimoteImage = QtGui.QLabel(self.wiimoteImageContainer)
        self.wiimoteImage.setGeometry(QtCore.QRect(0, 0, 157, 400))
        self.wiimoteImage.setText("")
        self.wiimoteImage.setPixmap(QtGui.QPixmap("images/wiimote.png"))
        self.wiimoteImage.setObjectName("wiimoteImage")
        self.btnA = QtGui.QLabel(self.wiimoteImageContainer)
        self.btnA.setGeometry(QtCore.QRect(100, 116, 17, 17))
        self.btnA.setText("")
        self.btnA.setPixmap(QtGui.QPixmap("images/button_highlight.png"))
        self.btnA.setObjectName("btnA")
        self.btnB = QtGui.QLabel(self.wiimoteImageContainer)
        self.btnB.setGeometry(QtCore.QRect(16, 129, 17, 17))
        self.btnB.setText("")
        self.btnB.setPixmap(QtGui.QPixmap("images/button_highlight.png"))
        self.btnB.setObjectName("btnB")
        self.btn1 = QtGui.QLabel(self.wiimoteImageContainer)
        self.btn1.setGeometry(QtCore.QRect(100, 285, 17, 17))
        self.btn1.setText("")
        self.btn1.setPixmap(QtGui.QPixmap("images/button_highlight.png"))
        self.btn1.setObjectName("btn1")
        self.btn2 = QtGui.QLabel(self.wiimoteImageContainer)
        self.btn2.setGeometry(QtCore.QRect(101, 321, 17, 17))
        self.btn2.setText("")
        self.btn2.setPixmap(QtGui.QPixmap("images/button_highlight.png"))
        self.btn2.setObjectName("btn2")
        self.btnMinus = QtGui.QLabel(self.wiimoteImageContainer)
        self.btnMinus.setGeometry(QtCore.QRect(73, 183, 17, 17))
        self.btnMinus.setText("")
        self.btnMinus.setPixmap(QtGui.QPixmap("images/button_highlight.png"))
        self.btnMinus.setObjectName("btnMinus")
        self.btnPlus = QtGui.QLabel(self.wiimoteImageContainer)
        self.btnPlus.setGeometry(QtCore.QRect(127, 182, 17, 17))
        self.btnPlus.setText("")
        self.btnPlus.setPixmap(QtGui.QPixmap("images/button_highlight.png"))
        self.btnPlus.setObjectName("btnPlus")
        self.btnHome = QtGui.QLabel(self.wiimoteImageContainer)
        self.btnHome.setGeometry(QtCore.QRect(100, 182, 17, 17))
        self.btnHome.setText("")
        self.btnHome.setPixmap(QtGui.QPixmap("images/button_highlight.png"))
        self.btnHome.setObjectName("btnHome")
        self.btnUp = QtGui.QLabel(self.wiimoteImageContainer)
        self.btnUp.setGeometry(QtCore.QRect(100, 42, 17, 17))
        self.btnUp.setText("")
        self.btnUp.setPixmap(QtGui.QPixmap("images/button_highlight.png"))
        self.btnUp.setObjectName("btnUp")
        self.btnRight = QtGui.QLabel(self.wiimoteImageContainer)
        self.btnRight.setGeometry(QtCore.QRect(114, 56, 17, 17))
        self.btnRight.setText("")
        self.btnRight.setPixmap(QtGui.QPixmap("images/button_highlight.png"))
        self.btnRight.setObjectName("btnRight")
        self.btnDown = QtGui.QLabel(self.wiimoteImageContainer)
        self.btnDown.setGeometry(QtCore.QRect(100, 71, 17, 17))
        self.btnDown.setText("")
        self.btnDown.setPixmap(QtGui.QPixmap("images/button_highlight.png"))
        self.btnDown.setObjectName("btnDown")
        self.btnLeft = QtGui.QLabel(self.wiimoteImageContainer)
        self.btnLeft.setGeometry(QtCore.QRect(85, 56, 17, 17))
        self.btnLeft.setText("")
        self.btnLeft.setPixmap(QtGui.QPixmap("images/button_highlight.png"))
        self.btnLeft.setObjectName("btnLeft")
        self.led1 = QtGui.QLabel(self.wiimoteImageContainer)
        self.led1.setGeometry(QtCore.QRect(77, 351, 11, 11))
        self.led1.setText("")
        self.led1.setPixmap(QtGui.QPixmap("images/led_highlight.png"))
        self.led1.setObjectName("led1")
        self.led4 = QtGui.QLabel(self.wiimoteImageContainer)
        self.led4.setGeometry(QtCore.QRect(130, 351, 11, 11))
        self.led4.setText("")
        self.led4.setPixmap(QtGui.QPixmap("images/led_highlight.png"))
        self.led4.setObjectName("led4")
        self.led3 = QtGui.QLabel(self.wiimoteImageContainer)
        self.led3.setGeometry(QtCore.QRect(112, 351, 11, 11))
        self.led3.setText("")
        self.led3.setPixmap(QtGui.QPixmap("images/led_highlight.png"))
        self.led3.setObjectName("led3")
        self.led2 = QtGui.QLabel(self.wiimoteImageContainer)
        self.led2.setGeometry(QtCore.QRect(95, 351, 11, 11))
        self.led2.setText("")
        self.led2.setPixmap(QtGui.QPixmap("images/led_highlight.png"))
        self.led2.setObjectName("led2")
        self.verticalLayout_2.addWidget(self.wiimoteImageContainer)
        self.label = QtGui.QLabel(self.statusGroupBox)
        self.label.setText("Battery")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.batteryProgressBar = QtGui.QProgressBar(self.statusGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.batteryProgressBar.sizePolicy().hasHeightForWidth())
        self.batteryProgressBar.setSizePolicy(sizePolicy)
        self.batteryProgressBar.setAutoFillBackground(False)
        self.batteryProgressBar.setProperty("value", 0)
        self.batteryProgressBar.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.batteryProgressBar.setObjectName("batteryProgressBar")
        self.verticalLayout_2.addWidget(self.batteryProgressBar)
        self.centreVerticalLayout.addWidget(self.statusGroupBox)
        spacerItem2 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.centreVerticalLayout.addItem(spacerItem2)
        self.horizontalLayout_4.addLayout(self.centreVerticalLayout)
        self.rightVerticalLayout = QtGui.QVBoxLayout()
        self.rightVerticalLayout.setObjectName("rightVerticalLayout")
        self.plotGroupBox = QtGui.QGroupBox(wiimoteTestQWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotGroupBox.sizePolicy().hasHeightForWidth())
        self.plotGroupBox.setSizePolicy(sizePolicy)
        self.plotGroupBox.setMinimumSize(QtCore.QSize(300, 200))
        self.plotGroupBox.setMaximumSize(QtCore.QSize(300, 200))
        self.plotGroupBox.setObjectName("plotGroupBox")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.plotGroupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.plotVerticalLayout = QtGui.QVBoxLayout()
        self.plotVerticalLayout.setObjectName("plotVerticalLayout")
        self.horizontalLayout_3.addLayout(self.plotVerticalLayout)
        self.rightVerticalLayout.addWidget(self.plotGroupBox)
        spacerItem3 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.rightVerticalLayout.addItem(spacerItem3)
        self.horizontalLayout_4.addLayout(self.rightVerticalLayout)
        spacerItem4 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.horizontalLayout_4.setStretch(3, 1)

        self.retranslateUi(wiimoteTestQWidget)
        QtCore.QMetaObject.connectSlotsByName(wiimoteTestQWidget)

    def retranslateUi(self, wiimoteTestQWidget):
        self.connectionGroupBox.setTitle(QtGui.QApplication.translate("wiimoteTestQWidget", "Bluetooth Connection", None, QtGui.QApplication.UnicodeUTF8))
        self.connectButton.setText(QtGui.QApplication.translate("wiimoteTestQWidget", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.disconnectButton.setText(QtGui.QApplication.translate("wiimoteTestQWidget", "Disconnect", None, QtGui.QApplication.UnicodeUTF8))
        self.controlGroupBox.setTitle(QtGui.QApplication.translate("wiimoteTestQWidget", "Wiimote Control", None, QtGui.QApplication.UnicodeUTF8))
        self.statusGroupBox.setTitle(QtGui.QApplication.translate("wiimoteTestQWidget", "Wiimote Status", None, QtGui.QApplication.UnicodeUTF8))
        self.plotGroupBox.setTitle(QtGui.QApplication.translate("wiimoteTestQWidget", "Plot", None, QtGui.QApplication.UnicodeUTF8))

