class ModAsignatura:
    def __init__(self,cod=0,descripcion='',codAsig ='',horas_semanales=1,creditos=0.0):
        self.__id = cod
        self.__descripcion = descripcion
        self.__codigo = codAsig
        self.__horas_semanales = horas_semanales
        self.__creditos =creditos

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,values):
        self.__id = values

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, values):
        self.__descripcion = values

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, values):
        self.__codigo = values

    @property
    def horas_semanales(self):
        return self.__horas_semanales

    @horas_semanales.setter
    def horas_semanales(self, values):
        self.__horas_semanales = values

    @property
    def creditos(self):
        return self.__creditos

    @creditos.setter
    def creditos(self, values):
        self.__creditos = values

