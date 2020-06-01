import json
import abc
class Personal:
    __Cuil=''
    __Apellido=''
    __Nombre=''
    __SueldoBasico=0.0
    __Antiguedad=0
    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad,carrera='',cargo='',catedra='',areainv='',tipoinv=''):
        self.__Cuil=cuil
        self.__Apellido=apellido
        self.__Nombre=nombre
        self.__SueldoBasico=int(sueldobasico)
        self.__Antiguedad=int(antiguedad)
    def __str__(self):
        cadena='Cuil {}\n'.format(self.__Cuil)
        cadena+='{} {}\n'.format(self.__Apellido,self.__Nombre)
        cadena+='$ {} con {} años de antiguedad'.format(self.__SueldoBasico,self.__Antiguedad)
        return cadena
    def getNombre(self):
        return self.__Nombre
    def getApellido(self):
        return self.__Apellido
    def getCuil(self):
        return self.__Cuil
    def getSueldoBasico(self):
        return self.__SueldoBasico
    def getAntiguedad(self):
        return self.__Antiguedad
    @abc.abstractmethod
    def toJson(self):
        pass    
