import pymysql


class Conector:
    def __init__(self, server='localhost', user='root', password='', database='horario'):
        self.__server = server
        self.__user = user
        self.__password = password
        self.__database = database
        self.__conn = ''
        self.__conector = ''

    def conectar(self):
        self.__conn = pymysql.connect(host=self.__server, user='root', password=self.__password, db = self.__database)
        self.__conector = self.__conn.cursor()
        #return self.__conector

    def cerrar(self):
        self.__conn.close()
        self.__conector.close()

    @property
    def conector(self):
        return self.__conector

    @property
    def conn(self):
        return self.__conn

    @property
    def user(self):
       return self.__user

c = Conector()
print(c.user)
