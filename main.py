from Docente import Docente
from DocenteInvestigador import DocenteInvestigador
from Apoyo import PersonalApoyo
from Investigador import Investigador
from Lista import ListaPersonal
from ObjectEnconder import ObjectEnconder




if __name__=="__main__":
    personal=ListaPersonal()
    Json=ObjectEnconder()
    dic=Json.LeerArchivo('Personal.json')
    personal=Json.DecodificarDiccionario(dic)
    for p in personal:
        print(p)
    
