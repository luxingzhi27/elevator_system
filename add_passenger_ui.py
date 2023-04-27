# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './add_passenger.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogAddPassenger(object):
    def setupUi(self, DialogAddPassenger):
        DialogAddPassenger.setObjectName("DialogAddPassenger")
        DialogAddPassenger.resize(400, 300)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(DialogAddPassenger)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(DialogAddPassenger)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(DialogAddPassenger)
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
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(DialogAddPassenger)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(DialogAddPassenger)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogAddPassenger)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogAddPassenger)
        self.buttonBox.accepted.connect(DialogAddPassenger.accept)
        self.buttonBox.rejected.connect(DialogAddPassenger.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogAddPassenger)

    def retranslateUi(self, DialogAddPassenger):
        _translate = QtCore.QCoreApplication.translate
        DialogAddPassenger.setWindowTitle(_translate("DialogAddPassenger", "AddPassenger"))
        self.label.setText(_translate("DialogAddPassenger", "current floor"))
        self.comboBox.setItemText(0, _translate("DialogAddPassenger", "1"))
        self.comboBox.setItemText(1, _translate("DialogAddPassenger", "2"))
        self.comboBox.setItemText(2, _translate("DialogAddPassenger", "3"))
        self.comboBox.setItemText(3, _translate("DialogAddPassenger", "4"))
        self.comboBox.setItemText(4, _translate("DialogAddPassenger", "5"))
        self.comboBox.setItemText(5, _translate("DialogAddPassenger", "6"))
        self.comboBox.setItemText(6, _translate("DialogAddPassenger", "7"))
        self.comboBox.setItemText(7, _translate("DialogAddPassenger", "8"))
        self.comboBox.setItemText(8, _translate("DialogAddPassenger", "9"))
        self.comboBox.setItemText(9, _translate("DialogAddPassenger", "10"))
        self.comboBox.setItemText(10, _translate("DialogAddPassenger", "11"))
        self.comboBox.setItemText(11, _translate("DialogAddPassenger", "12"))
        self.comboBox.setItemText(12, _translate("DialogAddPassenger", "13"))
        self.comboBox.setItemText(13, _translate("DialogAddPassenger", "14"))
        self.comboBox.setItemText(14, _translate("DialogAddPassenger", "15"))
        self.comboBox.setItemText(15, _translate("DialogAddPassenger", "16"))
        self.comboBox.setItemText(16, _translate("DialogAddPassenger", "17"))
        self.comboBox.setItemText(17, _translate("DialogAddPassenger", "18"))
        self.comboBox.setItemText(18, _translate("DialogAddPassenger", "19"))
        self.comboBox.setItemText(19, _translate("DialogAddPassenger", "20"))
        self.label_2.setText(_translate("DialogAddPassenger", "direction"))
        self.comboBox_2.setItemText(0, _translate("DialogAddPassenger", "up"))
        self.comboBox_2.setItemText(1, _translate("DialogAddPassenger", "down"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogAddPassenger = QtWidgets.QDialog()
    ui = Ui_DialogAddPassenger()
    ui.setupUi(DialogAddPassenger)
    DialogAddPassenger.show()
    sys.exit(app.exec_())

