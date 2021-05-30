import re
import sys
from _json import make_encoder

from PyQt5.QtWidgets import QApplication, QTableWidget, QMainWindow, QMessageBox, QDialog, QLabel, QLineEdit, \
    QTableWidgetItem
from PyQt5.QtGui import QFont
from PyQt5 import uic
from PyQt5.QtCore import Qt
import ctypes
from PyQt5.uic.properties import QtWidgets
from Asignaturas.ModAsignatura import ModAsignatura
from Asignaturas.CtrAsignatura import CtrAsignatura
ctr = CtrAsignatura()

#Formulario  Ingresar
class Formulario_Ingreso(QDialog):
    def __init__(self):
        #Inicializamos el Objeto QMain Window
        QDialog.__init__(self)
        #el metodo leadui permite trabajar con archivo ui en python
        uic.loadUi("Ingresar.ui",self)
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
        self.btn_guardar.clicked.connect(self.guardar)
        self.btn_cancelar.clicked.connect(self.volver)

    def guardar(self):
        self.descripcion = self.in_descripcion.text()
        self.codigo = self.in_codigo.text()
        self.horas = self.in_horas.text()
        self.creditos = self.in_creditos.text()
        self.creditos = float(self.creditos)
        self.horas = int(self.horas)
        self.id=0
        objeto=ModAsignatura(self.id,self.descripcion,self.codigo,self.horas,self.creditos)
        if ctr.ingresar(objeto) == True:
            QMessageBox.information(self, "Validacion Correcta", "Guardado Correctamente", QMessageBox.Discard)

        else:
            QMessageBox.warning(self, "Validacion Incorrecta", "Error al Guardar Correctamente", QMessageBox.Discard)

        self.in_descripcion.clear()
        self.in_codigo.clear()
        self.in_horas.clear()
        self.in_creditos.clear()


    def volver(self):
        self.hide()
#Formulario Buscar
class Formulario_Buscar(QDialog):
    def __init__(self):
        #Inicializamos el Objeto QMain Window
        QDialog.__init__(self)
        #el metodo leadui permite trabajar con archivo ui en python
        uic.loadUi("Buscar.ui",self)
        #Asignando titulo  al la ventana
        self.setWindowTitle('APP ASIGNATURA')
        #fijar el tamaño minimo de la ventana
        self.setMinimumSize(676,600)
        #fijar tamaño maximo
        self.setMaximumSize(676,600)
        #centrar ventana en el escritorio
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)
        left =  (resolucion_ancho/2)-(self.frameSize().width()/2)
        width = (resolucion_alto/2)-(self.frameSize().height()/2)
        self.move(left,width)
        self.btn_salir.clicked.connect(self.volver)
        self.btn_consultar.clicked.connect(self.Buscar)
    def Buscar(self):
        self.codigo = self.in_codigo.text()
        self.descripcion = self.in_descripcion.text()
        self.concul=ctr.buscar(self.codigo,self.descripcion)
        if  self.concul ==False:
            QMessageBox.warning(self, "Advertencia", "no existe esta asignatura", QMessageBox.Discard)
        self.tabla.setColumnCount(5)
        self.tabla.setHorizontalHeaderLabels(['ID','DESCRIPCION','CODIGO','HORAS/SEMANALES','CREDITOS'])
        for pos,valor  in enumerate(self.concul):
            self.tabla.insertRow(pos)
            self.id= QTableWidgetItem(str(valor[0]))
            self.descripcion = QTableWidgetItem(str(valor[1]))
            self.codigo = QTableWidgetItem(str(valor[2]))
            self.horas = QTableWidgetItem(str(valor[3]))
            self.creditos = QTableWidgetItem(str(valor[4]))
            self.tabla.setItem(pos,0,self.id)
            self.tabla.setItem(pos,1, self.descripcion)
            self.tabla.setItem(pos, 2, self.codigo)
            self.tabla.setItem(pos, 3, self.horas)
            self.tabla.setItem(pos, 4, self.creditos)
        self.in_descripcion.clear()
        self.in_codigo.clear()


    def volver(self):
        self.hide()
#Formulario Eliminar
class Formulario_Eliminar(QDialog):
    def __init__(self):
        #Inicializamos el Objeto QMain Window
        QDialog.__init__(self)
        #el metodo leadui permite trabajar con archivo ui en python
        uic.loadUi("Eliminar.ui",self)
        #Asignando titulo  al la ventana
        self.setWindowTitle('APP ASIGNATURA')
        #fijar el tamaño minimo de la ventana
        self.setMinimumSize(507,243)
        #fijar tamaño maximo
        self.setMaximumSize(507,243)
        #centrar ventana en el escritorio
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)
        left =  (resolucion_ancho/2)-(self.frameSize().width()/2)
        width = (resolucion_alto/2)-(self.frameSize().height()/2)
        self.move(left,width)
        self.btn_aceptar.clicked.connect(self.eliminar)
        self.btn_cancelar.clicked.connect(self.volver)

    def eliminar(self):
        self.id = self.in_id.text()
        self.id = int(self.id)
        if ctr.eliminar(self.id) ==True:
            QMessageBox.information(self,"Validacion Correcta","Guardado Correctamente",QMessageBox.Discard)
        else:
            QMessageBox.warning(self,"Validacion Incorrecta","Error al Guardado Correctamente",QMessageBox.Discard)
        self.in_id.clear()



    def volver(self):
        self.hide()

#Formulario Consultar
class Formulario_Consultar(QDialog):
    def __init__(self):
        #Inicializamos el Objeto QMain Window
        QDialog.__init__(self)
        #el metodo leadui permite trabajar con archivo ui en python
        uic.loadUi("Consultar.ui",self)
        #Asignando titulo  al la ventana
        self.setWindowTitle('APP ASIGNATURA')
        #fijar el tamaño minimo de la ventana
        self.setMinimumSize(710,418)
        #fijar tamaño maximo
        self.setMaximumSize(710,418)
        #centrar ventana en el escritorio
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)
        left =  (resolucion_ancho/2)-(self.frameSize().width()/2)
        width = (resolucion_alto/2)-(self.frameSize().height()/2)
        self.move(left,width)
        self.btn_salir.clicked.connect(self.volver)
        self.btn_consultar.clicked.connect(self.consultar)


    def consultar(self):
        self.concul=ctr.consulta()
        self.tabla.setColumnCount(5)
        self.tabla.setHorizontalHeaderLabels(['id','descripcion','codigo','horas','credito'])
        self.row =0
        for pos,valor  in enumerate(self.concul):
            self.tabla.insertRow(pos)
            self.id= QTableWidgetItem(str(valor[0]))
            self.descripcion = QTableWidgetItem(str(valor[1]))
            self.codigo = QTableWidgetItem(str(valor[2]))
            self.horas = QTableWidgetItem(str(valor[3]))
            self.creditos = QTableWidgetItem(str(valor[4]))
            self.tabla.setItem(pos,0,self.id)
            self.tabla.setItem(pos,1, self.descripcion)
            self.tabla.setItem(pos, 2, self.codigo)
            self.tabla.setItem(pos, 3, self.horas)
            self.tabla.setItem(pos, 4, self.creditos)



    def volver(self):
        self.hide()

    def closeEvent(self, event):
        resultado = QMessageBox.question(self, "Salir..", "¿Seguro que quieres salir de la aplicacion?",QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
class Formulario_Actualizar(QDialog):
    def __init__(self):
        #Inicializamos el Objeto QMain Window
        QDialog.__init__(self)
        #el metodo leadui permite trabajar con archivo ui en python
        uic.loadUi("Actualizar.ui",self)
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
        self.in_id.setText('0')
        self.btn_generar.clicked.connect(self.datos)
        self.btn_cancelar.clicked.connect(self.volver)
        self.btn_guardar.clicked.connect(self.actualizar)
    def datos(self):
        self.id = self.in_id.text()
        self.id = int(self.id)
        self.x= ctr.buscarId(self.id)
        if ctr.buscarId(self.id) == ():
            QMessageBox.warning(self, "Advertencia", "No existe ese Id",QMessageBox.Discard)
        else:
            for val in self.x:
                self.in_descripcion.setText(val[1])
                self.in_codigo.setText(val[2])
                self.in_horas.setText(str(val[3]))
                self.in_creditos.setText(str(val[4]))



    def actualizar(self):
        self.id = self.in_id.text()
        self.descripcion = self.in_descripcion.text()
        self.codigo = self.in_codigo.text()
        self.horas = self.in_horas.text()
        self.creditos = self.in_creditos.text()
        self.id = int(self.id)
        self.creditos = float(self.creditos)
        self.horas = int(self.horas)
        print(self.id, self.horas, self.creditos)
        objeto = ModAsignatura(self.id, self.descripcion, self.codigo, self.horas, self.creditos)
        if ctr.actualizar(objeto) ==True:
            QMessageBox.information(self, "Validacion Correcta", "Actualizado Correctamente", QMessageBox.Discard)
        else:
            QMessageBox.warning(self, "Validacion Incorrecta", "Error al Actualizado Correctamente", QMessageBox.Discard)
        self.in_descripcion.clear()
        self.in_codigo.clear()
        self.in_horas.clear()
        self.in_creditos.clear()
        self.in_id.setText('0')
    def volver(self):
        self.hide()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Formulario_Buscar()
    window.show()
    app.exec_()