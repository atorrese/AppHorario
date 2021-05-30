from Asignaturas.DaoAsignatura import DaoAsignatura

class CtrAsignatura(DaoAsignatura):
    def __init__(self ,obj = None):
        self.asignatura=obj

    def consulta(self):
        objDao = DaoAsignatura()
        return objDao.consultar()

    def ingresar(self,objeto):
        objDao  = DaoAsignatura()
        return  objDao.ingresar(objeto)

    def actualizar(self,objeto):
        objDao = DaoAsignatura()
        return  objDao.actualizar(objeto)

    def eliminar(self,id):
        objDao = DaoAsignatura()
        return objDao.eliminar(id)

    def buscar(self,codigo,descripcion):
        objeDao = DaoAsignatura()
        return objeDao.buscar(codigo,descripcion)

    def buscarId(self,id):
        objeDao = DaoAsignatura()
        return objeDao.buscarId(id)