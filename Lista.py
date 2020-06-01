from Nodo import Nodo
from Personal import Personal
from Docente import Docente
from Investigador import Investigador
from DocenteInvestigador import DocenteInvestigador
from Apoyo import PersonalApoyo
import json

class ListaPersonal:
  __comienzo=None
  __actual=None 
  __indice=0
  __tope=0
  def __init__(self):
      self.__comienzo=None
      self.__actual=None
  def __iter__(self):
      return self
  def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0            
            raise StopIteration    
        else:        
            dato=self.__actual.getDato()
            self.__indice+=1  
            self.__actual=self.__actual.getSiguiente()        
            return dato
  def AgregarPersonal(self,personal):
      try:
          if(type(personal)==Docente or (type(personal)==DocenteInvestigador) or (type(personal)==Investigador) or (type(personal)==PersonalApoyo)):
                nodo=Nodo(personal)
                if(self.__comienzo==None):
                    nodo.setSiguiente(self.__comienzo)
                    self.__comienzo=nodo
                    self.__actual=nodo
                    self.__tope+=1
                else:
                    aux=self.__comienzo
                    while(aux.getsiguiente()!=None):
                        aux=aux.getsiguiente()
                    nodo.setSiguiente(aux.getsiguiente)
                    aux.setSiguiente(nodo)
                    self.__tope+=1
          else:
              raise TypeError()
      except TypeError:
          print('No es agente')                
  def toJson(self):
      personal=[]
      for p in self:
          personal.append(p.toJson())
      d=dict(
          __class__=self.__class__.__name__,datos=personal
      )            
      return d
