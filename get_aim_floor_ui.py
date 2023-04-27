# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/luxingzhi/OneDriver/大二下/操作系统/进程项目/elevator/get_aim_floor.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogGetAimFloor(object):
    def setupUi(self, DialogGetAimFloor):
        DialogGetAimFloor.setObjectName("DialogGetAimFloor")
        DialogGetAimFloor.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogGetAimFloor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(DialogGetAimFloor)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(DialogGetAimFloor)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogGetAimFloor)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogGetAimFloor)
        self.buttonBox.accepted.connect(DialogGetAimFloor.accept)
        self.buttonBox.rejected.connect(DialogGetAimFloor.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogGetAimFloor)

    def retranslateUi(self, DialogGetAimFloor):
        _translate = QtCore.QCoreApplication.translate
        DialogGetAimFloor.setWindowTitle(_translate("DialogGetAimFloor", "choose aim floor"))
        self.label.setText(_translate("DialogGetAimFloor", "destination floor"))
        self.comboBox.setItemText(0, _translate("DialogGetAimFloor", "1"))
        self.comboBox.setItemText(1, _translate("DialogGetAimFloor", "2"))
        self.comboBox.setItemText(2, _translate("DialogGetAimFloor", "3"))
        self.comboBox.setItemText(3, _translate("DialogGetAimFloor", "4"))
        self.comboBox.setItemText(4, _translate("DialogGetAimFloor", "5"))
        self.comboBox.setItemText(5, _translate("DialogGetAimFloor", "6"))
        self.comboBox.setItemText(6, _translate("DialogGetAimFloor", "7"))
        self.comboBox.setItemText(7, _translate("DialogGetAimFloor", "8"))
        self.comboBox.setItemText(8, _translate("DialogGetAimFloor", "9"))
        self.comboBox.setItemText(9, _translate("DialogGetAimFloor", "10"))
        self.comboBox.setItemText(10, _translate("DialogGetAimFloor", "11"))
        self.comboBox.setItemText(11, _translate("DialogGetAimFloor", "12"))
        self.comboBox.setItemText(12, _translate("DialogGetAimFloor", "13"))
        self.comboBox.setItemText(13, _translate("DialogGetAimFloor", "14"))
        self.comboBox.setItemText(14, _translate("DialogGetAimFloor", "15"))
        self.comboBox.setItemText(15, _translate("DialogGetAimFloor", "16"))
        self.comboBox.setItemText(16, _translate("DialogGetAimFloor", "17"))
        self.comboBox.setItemText(17, _translate("DialogGetAimFloor", "18"))
        self.comboBox.setItemText(18, _translate("DialogGetAimFloor", "19"))
        self.comboBox.setItemText(19, _translate("DialogGetAimFloor", "20"))

