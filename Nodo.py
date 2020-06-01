from Personal import Personal
from Investigador import Investigador
from Docente import Docente
from DocenteInvestigador import DocenteInvestigador
from Apoyo import PersonalApoyo
class Nodo:
    __Personal=None
    __Siguiente=None
    def __init__(self,personal):
        self.__Personal=personal
        self.__Siguiente=None
    def getsiguiente(self):
        return self.__Siguiente
    def setSiguiente(self,siguiente):
        self.__Siguiente=siguiente
    def getDato(self):
        return self.__Personal
