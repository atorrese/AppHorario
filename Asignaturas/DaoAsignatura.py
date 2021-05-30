from Conexion import Conector

class DaoAsignatura(Conector):
    def __init__(self, server='localhost', user=' root', password='', database='horario'):
        super().__init__(server, user, password, database)

    def consultar(self):
        result = False
        try:
            sql = "SELECT * FROM HOR_ASIGNATURA"
            self.conectar()
            self.conector.execute(sql)
            result = self.conector.fetchall()
            self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            self.cerrar()
        return result

    def ingresar(self,objeto):
        ok = True
        try:
            '''self.__id = cod
        self.__descripcion = descripcion
        self.__codigo = codAsig
        self.__horas_semanales = horas_semanales
        self.__creditos =creditos'''
            sql = "INSERT INTO HOR_ASIGNATURA(ASIGDESCRIPCION,ASIGCODIGO,ASIGHORASSEMANALES,ASIGNUMEROCREDITOS) VALUES(%s,%s,%s,%s)"
            self.conectar()
            self.conector.execute(sql,(objeto.descripcion,objeto.codigo,objeto.horas_semanales,objeto.creditos))
            self.conn.commit()
        except:
            ok = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return ok


    def eliminar(self,id):
        ok  = True
        try:
            sql = "DELETE FROM HOR_ASIGNATURA WHERE ASIGID = %s "
            self.conectar()
            self.conector.execute(sql,(id))
            self.conn.commit()
        except:
            ok= False
            self.conn.rollback()
        finally:
            self.cerrar()
        return ok

    def actualizar(self,objeto):
        ok  = True
        try:
            sql = "UPDATE HOR_ASIGNATURA  SET ASIGDESCRIPCION =%s ,ASIGCODIGO =%s , ASIGHORASSEMANALES= %s,ASIGNUMEROCREDITOS=%s WHERE ASIGID =%s"
            self.conectar()
            self.conector.execute(sql,(objeto.descripcion,objeto.codigo,objeto.horas_semanales,objeto.creditos,objeto.id))
            self.conn.commit()
        except:
            ok= False
            self.conn.rollback()
        finally:
            self.cerrar()
        return ok

    def buscar(self,codigo,descripcion):
        try:
            sql = "SELECT  * FROM HOR_ASIGNATURA WHERE ASIGCODIGO =%s OR ASIGdESCRIPCION=%s "
            self.conectar()
            self.conector.execute(sql,(codigo,descripcion))
            result = self.conector.fetchall()
            self.conn.commit()
        except:
            result = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return result

    def buscarId(self,id):
        result = False
        try:
            sql = "SELECT  * FROM HOR_ASIGNATURA WHERE ASIGID=%s"
            self.conectar()
            self.conector.execute(sql,(id))
            result = self.conector.fetchall()
            self.conn.commit()
        except:
            result = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return result
