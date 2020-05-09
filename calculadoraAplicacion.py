import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QWidget,QPushButton

from calculadora import calculadora


class CalculadoraAplicacion(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = calculadora()
        self.ui.setupUi(self)

        self.ui.btn_suma.clicked.connect(self.adicion)
        self.ui.btn_resta.clicked.connect(self.diferencia)
        self.ui.btn_mult.clicked.connect(self.mult)
        self.ui.btn_div.clicked.connect(self.div)

        self.show()

    def adicion(self):
        suma = 0
        op1 = 0
        op2 = 0
        if len(self.ui.txt_uno.text()) > 0:
            op1 = int(self.ui.txt_uno.text())
        if len(self.ui.txt_dos.text()) > 0:
            op2 = int(self.ui.txt_uno.text())
        suma = op1 + op2

        self.ui.txt_salida.text(str(suma))

    def diferencia(self):
        resta = 0
        op1 = 0
        op2 = 0
        if len(self.ui.txt_uno.text()) > 0:
            op1 = int(self.ui.txt_uno.text())
        if len(self.ui.txt_dos.text()) > 0:
            op2 = int(self.ui.txt_uno.text())
        resta = op1 - op2

        self.ui.txt_salida.text(str(resta))

    def mult(self):
        multiplo = 0
        op1 = 0
        op2 = 0
        if len(self.ui.txt_uno.text()) > 0:
            op1 = int(self.ui.txt_uno.text())
        if len(self.ui.txt_dos.text()) > 0:
            op2 = int(self.ui.txt_uno.text())
        multiplo = op1 * op2
        self.ui.txt_salida.text(str(multiplo))

    def div(self):
        dividir = 0
        op1 = 0
        op2 = 0
        if len(self.ui.txt_uno.text()) > 0:
            op1 = int(self.ui.txt_uno.text())
        if len(self.ui.txt_dos.text()) > 0:
            op2 = int(self.ui.txt_uno.text())
        dividir = op1 / op2

        self.ui.txt_salida.text(str(dividir))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = CalculadoraAplicacion()
    dialogo.show()
    sys.exit(app.exec_())
