# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './elevator.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(922, 260)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.aboutButton = QtWidgets.QPushButton(self.widget)
        self.aboutButton.setObjectName("aboutButton")
        self.verticalLayout_9.addWidget(self.aboutButton)
        self.resetButton = QtWidgets.QPushButton(self.widget)
        self.resetButton.setObjectName("resetButton")
        self.verticalLayout_9.addWidget(self.resetButton)
        self.addPassengerButton = QtWidgets.QPushButton(self.widget)
        self.addPassengerButton.setObjectName("addPassengerButton")
        self.verticalLayout_9.addWidget(self.addPassengerButton)
        self.verticalLayout_5.addWidget(self.widget)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.lcdNumber_1 = QtWidgets.QLCDNumber(self.widget_3)
        self.lcdNumber_1.setObjectName("lcdNumber_1")
        self.verticalLayout_11.addWidget(self.lcdNumber_1)
        self.elevator1OpenButton = QtWidgets.QPushButton(self.widget_3)
        self.elevator1OpenButton.setObjectName("elevator1OpenButton")
        self.verticalLayout_11.addWidget(self.elevator1OpenButton)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.elevator1UpButton = QtWidgets.QPushButton(self.widget_3)
        self.elevator1UpButton.setObjectName("elevator1UpButton")
        self.horizontalLayout_2.addWidget(self.elevator1UpButton)
        self.elevator1DownButton = QtWidgets.QPushButton(self.widget_3)
        self.elevator1DownButton.setObjectName("elevator1DownButton")
        self.horizontalLayout_2.addWidget(self.elevator1DownButton)
        self.verticalLayout_11.addLayout(self.horizontalLayout_2)
        self.elevator1EnterButton = QtWidgets.QPushButton(self.widget_3)
        self.elevator1EnterButton.setObjectName("elevator1EnterButton")
        self.verticalLayout_11.addWidget(self.elevator1EnterButton)
        self.verticalLayout.addWidget(self.widget_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_6 = QtWidgets.QWidget(self.centralwidget)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.widget_6)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.verticalLayout_12.addWidget(self.lcdNumber_2)
        self.elevator2OpenButton = QtWidgets.QPushButton(self.widget_6)
        self.elevator2OpenButton.setObjectName("elevator2OpenButton")
        self.verticalLayout_12.addWidget(self.elevator2OpenButton)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.elevator2UpButton = QtWidgets.QPushButton(self.widget_6)
        self.elevator2UpButton.setObjectName("elevator2UpButton")
        self.horizontalLayout_3.addWidget(self.elevator2UpButton)
        self.elevator2DownButton = QtWidgets.QPushButton(self.widget_6)
        self.elevator2DownButton.setObjectName("elevator2DownButton")
        self.horizontalLayout_3.addWidget(self.elevator2DownButton)
        self.verticalLayout_12.addLayout(self.horizontalLayout_3)
        self.elevator2EnterButton = QtWidgets.QPushButton(self.widget_6)
        self.elevator2EnterButton.setObjectName("elevator2EnterButton")
        self.verticalLayout_12.addWidget(self.elevator2EnterButton)
        self.verticalLayout_4.addWidget(self.widget_6)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_8 = QtWidgets.QWidget(self.centralwidget)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.widget_8)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.verticalLayout_13.addWidget(self.lcdNumber_3)
        self.elevator3OpenButton = QtWidgets.QPushButton(self.widget_8)
        self.elevator3OpenButton.setObjectName("elevator3OpenButton")
        self.verticalLayout_13.addWidget(self.elevator3OpenButton)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.elevator3UpButton = QtWidgets.QPushButton(self.widget_8)
        self.elevator3UpButton.setObjectName("elevator3UpButton")
        self.horizontalLayout_4.addWidget(self.elevator3UpButton)
        self.elevator3DownButton = QtWidgets.QPushButton(self.widget_8)
        self.elevator3DownButton.setObjectName("elevator3DownButton")
        self.horizontalLayout_4.addWidget(self.elevator3DownButton)
        self.verticalLayout_13.addLayout(self.horizontalLayout_4)
        self.elevator3EnterButton = QtWidgets.QPushButton(self.widget_8)
        self.elevator3EnterButton.setObjectName("elevator3EnterButton")
        self.verticalLayout_13.addWidget(self.elevator3EnterButton)
        self.verticalLayout_6.addWidget(self.widget_8)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_10 = QtWidgets.QWidget(self.centralwidget)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.widget_10)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.verticalLayout_14.addWidget(self.lcdNumber_4)
        self.elevator4OpenButton = QtWidgets.QPushButton(self.widget_10)
        self.elevator4OpenButton.setObjectName("elevator4OpenButton")
        self.verticalLayout_14.addWidget(self.elevator4OpenButton)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.elevator4UpButton = QtWidgets.QPushButton(self.widget_10)
        self.elevator4UpButton.setObjectName("elevator4UpButton")
        self.horizontalLayout_5.addWidget(self.elevator4UpButton)
        self.elevator4DownButton = QtWidgets.QPushButton(self.widget_10)
        self.elevator4DownButton.setObjectName("elevator4DownButton")
        self.horizontalLayout_5.addWidget(self.elevator4DownButton)
        self.verticalLayout_14.addLayout(self.horizontalLayout_5)
        self.elevator4EnterButton = QtWidgets.QPushButton(self.widget_10)
        self.elevator4EnterButton.setObjectName("elevator4EnterButton")
        self.verticalLayout_14.addWidget(self.elevator4EnterButton)
        self.verticalLayout_3.addWidget(self.widget_10)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_12 = QtWidgets.QWidget(self.centralwidget)
        self.widget_12.setObjectName("widget_12")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.widget_12)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.widget_12)
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.verticalLayout_15.addWidget(self.lcdNumber_5)
        self.elevator5OpenButton = QtWidgets.QPushButton(self.widget_12)
        self.elevator5OpenButton.setObjectName("elevator5OpenButton")
        self.verticalLayout_15.addWidget(self.elevator5OpenButton)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.elevator5UpButton = QtWidgets.QPushButton(self.widget_12)
        self.elevator5UpButton.setObjectName("elevator5UpButton")
        self.horizontalLayout_6.addWidget(self.elevator5UpButton)
        self.elevator5DownButton = QtWidgets.QPushButton(self.widget_12)
        self.elevator5DownButton.setObjectName("elevator5DownButton")
        self.horizontalLayout_6.addWidget(self.elevator5DownButton)
        self.verticalLayout_15.addLayout(self.horizontalLayout_6)
        self.elevator5EnterButton = QtWidgets.QPushButton(self.widget_12)
        self.elevator5EnterButton.setObjectName("elevator5EnterButton")
        self.verticalLayout_15.addWidget(self.elevator5EnterButton)
        self.verticalLayout_2.addWidget(self.widget_12)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "elevator system"))
        self.aboutButton.setText(_translate("MainWindow", "About"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.addPassengerButton.setText(_translate("MainWindow", "Add passenger"))
        self.elevator1OpenButton.setText(_translate("MainWindow", "open"))
        self.elevator1UpButton.setText(_translate("MainWindow", "up"))
        self.elevator1DownButton.setText(_translate("MainWindow", "down"))
        self.elevator1EnterButton.setText(_translate("MainWindow", "enter"))
        self.elevator2OpenButton.setText(_translate("MainWindow", "open"))
        self.elevator2UpButton.setText(_translate("MainWindow", "up"))
        self.elevator2DownButton.setText(_translate("MainWindow", "down"))
        self.elevator2EnterButton.setText(_translate("MainWindow", "enter"))
        self.elevator3OpenButton.setText(_translate("MainWindow", "open"))
        self.elevator3UpButton.setText(_translate("MainWindow", "up"))
        self.elevator3DownButton.setText(_translate("MainWindow", "down"))
        self.elevator3EnterButton.setText(_translate("MainWindow", "enter"))
        self.elevator4OpenButton.setText(_translate("MainWindow", "open"))
        self.elevator4UpButton.setText(_translate("MainWindow", "up"))
        self.elevator4DownButton.setText(_translate("MainWindow", "down"))
        self.elevator4EnterButton.setText(_translate("MainWindow", "enter"))
        self.elevator5OpenButton.setText(_translate("MainWindow", "open"))
        self.elevator5UpButton.setText(_translate("MainWindow", "up"))
        self.elevator5DownButton.setText(_translate("MainWindow", "down"))
        self.elevator5EnterButton.setText(_translate("MainWindow", "enter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

