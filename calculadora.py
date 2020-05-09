# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculadora.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class calculadora(object):
    def setupUi(self, calculadora):
        calculadora.setObjectName("calculadora")
        calculadora.resize(399, 240)
        self.lbl_primer = QtWidgets.QLabel(calculadora)
        self.lbl_primer.setGeometry(QtCore.QRect(13, 10, 161, 20))
        self.lbl_primer.setObjectName("lbl_primer")
        self.lbl_segundo = QtWidgets.QLabel(calculadora)
        self.lbl_segundo.setGeometry(QtCore.QRect(13, 60, 181, 20))
        self.lbl_segundo.setObjectName("lbl_segundo")
        self.txt_uno = QtWidgets.QLineEdit(calculadora)
        self.txt_uno.setGeometry(QtCore.QRect(270, 10, 113, 25))
        self.txt_uno.setObjectName("txt_uno")
        self.txt_dos = QtWidgets.QLineEdit(calculadora)
        self.txt_dos.setGeometry(QtCore.QRect(270, 60, 113, 25))
        self.txt_dos.setObjectName("txt_dos")
        self.btn_resta = QtWidgets.QPushButton(calculadora)
        self.btn_resta.setGeometry(QtCore.QRect(30, 110, 31, 31))
        self.btn_resta.setObjectName("btn_resta")
        self.btn_suma = QtWidgets.QPushButton(calculadora)
        self.btn_suma.setGeometry(QtCore.QRect(140, 110, 31, 31))
        self.btn_suma.setObjectName("btn_suma")
        self.btn_mult = QtWidgets.QPushButton(calculadora)
        self.btn_mult.setGeometry(QtCore.QRect(230, 110, 31, 31))
        self.btn_mult.setObjectName("btn_mult")
        self.btn_div = QtWidgets.QPushButton(calculadora)
        self.btn_div.setGeometry(QtCore.QRect(330, 110, 31, 31))
        self.btn_div.setObjectName("btn_div")
        self.txt_salida = QtWidgets.QLabel(calculadora)
        self.txt_salida.setGeometry(QtCore.QRect(80, 180, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.txt_salida.setFont(font)
        self.txt_salida.setText("")
        self.txt_salida.setObjectName("txt_salida")

        self.retranslateUi(calculadora)
        QtCore.QMetaObject.connectSlotsByName(calculadora)

    def retranslateUi(self, calculadora):
        _translate = QtCore.QCoreApplication.translate
        calculadora.setWindowTitle(_translate("calculadora", "Calculadora Basica"))
        self.lbl_primer.setText(_translate("calculadora", "ingrese primer operando"))
        self.lbl_segundo.setText(_translate("calculadora", "ingrese segundo operando"))
        self.btn_resta.setText(_translate("calculadora", "-"))
        self.btn_suma.setText(_translate("calculadora", "+"))
        self.btn_mult.setText(_translate("calculadora", "*"))
        self.btn_div.setText(_translate("calculadora", "/"))
