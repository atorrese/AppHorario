import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QLabel
from PyQt5.QtGui import QFont
from PyQt5 import uic
from PyQt5.QtCore import Qt
import ctypes
from Asignaturas.Pantallas.Formularios import Formulario_Ingreso,Formulario_Buscar,Formulario_Eliminar,Formulario_Consultar,Formulario_Actualizar

from PyQt5.uic.properties import QtWidgets
class Ventana_Asignatura(QMainWindow):
    def __init__(self):
        #Inicializamos el Objeto QMain Window
        QMainWindow.__init__(self)
        #el metodo leadui permite trabajar con archivo ui en python
        uic.loadUi("Menu_opciones.ui",self)
        #Asignando titulo  al la ventana
        self.setWindowTitle('APP ASIGNATURA')
        #fijar el tamaño minimo de la ventana
        self.setMinimumSize(500,500)
        #fijar tamaño maximo
        self.setMaximumSize(500,500)
        #centrar ventana en el escritorio
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)
        left =  (resolucion_ancho/2)-(self.frameSize().width()/2)
        width = (resolucion_alto/2)-(self.frameSize().height()/2)
        self.move(left,width)
        self.btn_ingresar.clicked.connect(self.ingresar)
        self.btn_consultar.clicked.connect(self.consultar)
        self.btn_buscar.clicked.connect(self.buscar)
        self.btn_volver.clicked.connect(self.volver)
        self.btn_eliminar.clicked.connect(self.eliminar)
        self.btn_editar.clicked.connect(self.actualizar)
    def ingresar(self):
        self.mostrar =  Formulario_Ingreso()
        self.mostrar.show()
        self.mostrar.exec_()
    def consultar(self):
        self.mostrar = Formulario_Consultar()
        self.mostrar.show()
        self.mostrar.exec_()
    def buscar(self):
        self.mostrar = Formulario_Buscar()
        self.mostrar.show
        self.mostrar.exec_()
    def eliminar(self):
        self.mostrar = Formulario_Eliminar()
        self.mostrar.show()
        self.mostrar.exec_()
    def actualizar(self):
        self.mostrar = Formulario_Actualizar()
        self.mostrar.show()
        self.mostrar.exec_()
    def volver(self):
        self.hide()



    def cerrar(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ventana_Asignatura()
    window.show()
    app.exec_()
