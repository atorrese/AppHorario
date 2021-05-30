import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QLabel
from PyQt5.QtGui import QFont
from PyQt5 import uic
from PyQt5.QtCore import Qt
import ctypes
from Asignaturas.Pantallas.Menu_Asignatura import Ventana_Asignatura

from PyQt5.uic.properties import QtWidgets
class Ventana_principal(QMainWindow,QApplication):
    def __init__(self):
        #Inicializamos el Objeto QMain Window
        QMainWindow.__init__(self)
        #el metodo leadui permite trabajar co  n archivo ui en python
        uic.loadUi("principal.ui",self)
        #Asignando titulo  al la ventana
        self.setWindowTitle('APP ASIGNATURA')
        #fijar el tamaño minimo de la ventana
        self.setMinimumSize(200,200)
        #fijar tamaño maximo
        self.setMaximumSize(200,200)
        #centrar ventana en el escritorio
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)
        left =  (resolucion_ancho/2)-(self.frameSize().width()/2)
        width = (resolucion_alto/2)-(self.frameSize().height()/2)
        self.move(left,width)
        self.btn_Asignatura.clicked.connect(self.abrirse)
        self.btn_salir.clicked.connect(self.cerrar)

    def abrirse(self):
        self.mostrar = Ventana_Asignatura()
        self.mostrar.show()

    def cerrar(self):
        self.close()



    def closeEvent(self, event):
        resultado = QMessageBox.question(self, "Salir..", "¿Seguro que quieres salir de la aplicacion?",QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ventana_principal()
    window.show()
    app.exec_()
