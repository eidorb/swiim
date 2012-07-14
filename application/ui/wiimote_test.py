from PySide import QtCore, QtGui

class Ui_wiimoteTestQWidget(object):
    def setupUi(self, wiimoteTestQWidget):
        wiimoteTestQWidget.setObjectName("wiimoteTestQWidget")
        wiimoteTestQWidget.resize(387, 505)
        self.horizontalLayout_4 = QtGui.QHBoxLayout(wiimoteTestQWidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBoxLayout = QtGui.QVBoxLayout()
        self.groupBoxLayout.setObjectName("groupBoxLayout")
        self.connectionGroup = QtGui.QGroupBox(wiimoteTestQWidget)
        self.connectionGroup.setObjectName("connectionGroup")
        self.horizontalLayout = QtGui.QHBoxLayout(self.connectionGroup)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.connect = QtGui.QPushButton(self.connectionGroup)
        self.connect.setObjectName("connect")
        self.horizontalLayout.addWidget(self.connect)
        self.disconnect = QtGui.QPushButton(self.connectionGroup)
        self.disconnect.setObjectName("disconnect")
        self.horizontalLayout.addWidget(self.disconnect)
        self.groupBoxLayout.addWidget(self.connectionGroup)
        self.controlGroup = QtGui.QGroupBox(wiimoteTestQWidget)
        self.controlGroup.setEnabled(True)
        self.controlGroup.setObjectName("controlGroup")
        self.verticalLayout = QtGui.QVBoxLayout(self.controlGroup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.controlRumble = QtGui.QPushButton(self.controlGroup)
        self.controlRumble.setText("Toggle Rumble")
        self.controlRumble.setObjectName("controlRumble")
        self.verticalLayout.addWidget(self.controlRumble)
        self.label_2 = QtGui.QLabel(self.controlGroup)
        self.label_2.setText("Set LEDs")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.controlLed1 = QtGui.QCheckBox(self.controlGroup)
        self.controlLed1.setText("")
        self.controlLed1.setChecked(False)
        self.controlLed1.setObjectName("controlLed1")
        self.horizontalLayout_2.addWidget(self.controlLed1)
        self.controlLed2 = QtGui.QCheckBox(self.controlGroup)
        self.controlLed2.setText("")
        self.controlLed2.setObjectName("controlLed2")
        self.horizontalLayout_2.addWidget(self.controlLed2)
        self.controlLed3 = QtGui.QCheckBox(self.controlGroup)
        self.controlLed3.setText("")
        self.controlLed3.setObjectName("controlLed3")
        self.horizontalLayout_2.addWidget(self.controlLed3)
        self.controlLed4 = QtGui.QCheckBox(self.controlGroup)
        self.controlLed4.setText("")
        self.controlLed4.setObjectName("controlLed4")
        self.horizontalLayout_2.addWidget(self.controlLed4)
        spacerItem = QtGui.QSpacerItem(72, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.groupBoxLayout.addWidget(self.controlGroup)
        spacerItem1 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.groupBoxLayout.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.groupBoxLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.statusGroup = QtGui.QGroupBox(wiimoteTestQWidget)
        self.statusGroup.setObjectName("statusGroup")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.statusGroup)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.wiimoteImageHolder = QtGui.QWidget(self.statusGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wiimoteImageHolder.sizePolicy().hasHeightForWidth())
        self.wiimoteImageHolder.setSizePolicy(sizePolicy)
        self.wiimoteImageHolder.setMinimumSize(QtCore.QSize(157, 400))
        self.wiimoteImageHolder.setMaximumSize(QtCore.QSize(157, 400))
        self.wiimoteImageHolder.setObjectName("wiimoteImageHolder")
        self.wiimoteImage = QtGui.QLabel(self.wiimoteImageHolder)
        self.wiimoteImage.setGeometry(QtCore.QRect(0, 0, 157, 400))
        self.wiimoteImage.setText("")
        self.wiimoteImage.setPixmap(QtGui.QPixmap("images/wiimote.png"))
        self.wiimoteImage.setObjectName("wiimoteImage")
        self.btnA = QtGui.QLabel(self.wiimoteImageHolder)
        self.btnA.setGeometry(QtCore.QRect(100, 116, 17, 17))
        self.btnA.setText("")
        self.btnA.setPixmap(QtGui.QPixmap("images/button_highlight.png"))
        self.btnA.setObjectName("btnA")
        self.btnB = QtGui.QLabel(self.wiimoteImageHolder)
        self.btnB.setGeometry(QtCore.QRect(16, 129, 17, 17))
        self.btnB.setText("")
        self.btnB.setPixmap(QtGui.QPixmap("images/button_highlight.png"))
        self.btnB.setObjectName("btnB")
        self.btn1 = QtGui.QLabel(self.wiimoteImageHolder)
        self.btn1.setGeometry(QtCore.QRect(100, 285, 17, 17))
        self.btn1.setText("")
        self.btn1.setPixmap(QtGui.QPixmap("images/button_highlight.png"))
        self.btn1.setObjectName("btn1")
        self.btn2 = QtGui.QLabel(self.wiimoteImageHolder)
        self.btn2.setGeometry(QtCore.QRect(101, 321, 17, 17))
        self.btn2.setText("")
        self.btn2.setPixmap(QtGui.QPixmap("images/button_highlight.png"))
        self.btn2.setObjectName("btn2")
        self.btnMinus = QtGui.QLabel(self.wiimoteImageHolder)
        self.btnMinus.setGeometry(QtCore.QRect(73, 183, 17, 17))
        self.btnMinus.setText("")
        self.btnMinus.setPixmap(QtGui.QPixmap("images/button_highlight.png"))
        self.btnMinus.setObjectName("btnMinus")
        self.btnPlus = QtGui.QLabel(self.wiimoteImageHolder)
        self.btnPlus.setGeometry(QtCore.QRect(127, 182, 17, 17))
        self.btnPlus.setText("")
        self.btnPlus.setPixmap(QtGui.QPixmap("images/button_highlight.png"))
        self.btnPlus.setObjectName("btnPlus")
        self.btnHome = QtGui.QLabel(self.wiimoteImageHolder)
        self.btnHome.setGeometry(QtCore.QRect(100, 182, 17, 17))
        self.btnHome.setText("")
        self.btnHome.setPixmap(QtGui.QPixmap("images/button_highlight.png"))
        self.btnHome.setObjectName("btnHome")
        self.btnUp = QtGui.QLabel(self.wiimoteImageHolder)
        self.btnUp.setGeometry(QtCore.QRect(100, 42, 17, 17))
        self.btnUp.setText("")
        self.btnUp.setPixmap(QtGui.QPixmap("images/button_highlight.png"))
        self.btnUp.setObjectName("btnUp")
        self.btnRight = QtGui.QLabel(self.wiimoteImageHolder)
        self.btnRight.setGeometry(QtCore.QRect(114, 56, 17, 17))
        self.btnRight.setText("")
        self.btnRight.setPixmap(QtGui.QPixmap("images/button_highlight.png"))
        self.btnRight.setObjectName("btnRight")
        self.btnDown = QtGui.QLabel(self.wiimoteImageHolder)
        self.btnDown.setGeometry(QtCore.QRect(100, 71, 17, 17))
        self.btnDown.setText("")
        self.btnDown.setPixmap(QtGui.QPixmap("images/button_highlight.png"))
        self.btnDown.setObjectName("btnDown")
        self.btnLeft = QtGui.QLabel(self.wiimoteImageHolder)
        self.btnLeft.setGeometry(QtCore.QRect(85, 56, 17, 17))
        self.btnLeft.setText("")
        self.btnLeft.setPixmap(QtGui.QPixmap("images/button_highlight.png"))
        self.btnLeft.setObjectName("btnLeft")
        self.led1 = QtGui.QLabel(self.wiimoteImageHolder)
        self.led1.setGeometry(QtCore.QRect(77, 351, 11, 11))
        self.led1.setText("")
        self.led1.setPixmap(QtGui.QPixmap("images/led_highlight.png"))
        self.led1.setObjectName("led1")
        self.led4 = QtGui.QLabel(self.wiimoteImageHolder)
        self.led4.setGeometry(QtCore.QRect(130, 351, 11, 11))
        self.led4.setText("")
        self.led4.setPixmap(QtGui.QPixmap("images/led_highlight.png"))
        self.led4.setObjectName("led4")
        self.led3 = QtGui.QLabel(self.wiimoteImageHolder)
        self.led3.setGeometry(QtCore.QRect(112, 351, 11, 11))
        self.led3.setText("")
        self.led3.setPixmap(QtGui.QPixmap("images/led_highlight.png"))
        self.led3.setObjectName("led3")
        self.led2 = QtGui.QLabel(self.wiimoteImageHolder)
        self.led2.setGeometry(QtCore.QRect(95, 351, 11, 11))
        self.led2.setText("")
        self.led2.setPixmap(QtGui.QPixmap("images/led_highlight.png"))
        self.led2.setObjectName("led2")
        self.verticalLayout_2.addWidget(self.wiimoteImageHolder)
        self.label = QtGui.QLabel(self.statusGroup)
        self.label.setText("Battery")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.statusBattery = QtGui.QProgressBar(self.statusGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusBattery.sizePolicy().hasHeightForWidth())
        self.statusBattery.setSizePolicy(sizePolicy)
        self.statusBattery.setAutoFillBackground(False)
        self.statusBattery.setProperty("value", 0)
        self.statusBattery.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.statusBattery.setObjectName("statusBattery")
        self.verticalLayout_2.addWidget(self.statusBattery)
        self.verticalLayout_3.addWidget(self.statusGroup)
        spacerItem2 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem3 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)

        self.retranslateUi(wiimoteTestQWidget)
        QtCore.QMetaObject.connectSlotsByName(wiimoteTestQWidget)

    def retranslateUi(self, wiimoteTestQWidget):
        self.connectionGroup.setTitle(QtGui.QApplication.translate("wiimoteTestQWidget", "Bluetooth Connection", None, QtGui.QApplication.UnicodeUTF8))
        self.connect.setText(QtGui.QApplication.translate("wiimoteTestQWidget", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.disconnect.setText(QtGui.QApplication.translate("wiimoteTestQWidget", "Disconnect", None, QtGui.QApplication.UnicodeUTF8))
        self.controlGroup.setTitle(QtGui.QApplication.translate("wiimoteTestQWidget", "Wiimote Control", None, QtGui.QApplication.UnicodeUTF8))
        self.statusGroup.setTitle(QtGui.QApplication.translate("wiimoteTestQWidget", "Wiimote Status", None, QtGui.QApplication.UnicodeUTF8))

