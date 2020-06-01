from zope.interface import Interface

class Iejercicio(Interface):
    def InsertarElemento(self,pos,elemento):
        pass
    def AgregarPersonal(self,personal):
        pass
    def MostrarElemento(self):
        pass
    
