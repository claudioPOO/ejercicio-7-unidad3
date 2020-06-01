import json
from pathlib import Path
from Docente import Docente
from DocenteInvestigador import DocenteInvestigador
from Apoyo import PersonalApoyo
from Investigador import Investigador
from Lista import ListaPersonal
from Personal import Personal
class ObjectEnconder(object):
 def GuardarArchivo(self,dic,archivo):
    with Path(archivo).open("w",encoding="UTF-8")as destino:
        json.dump(dic,destino,indent=4)
        destino.close()
 def LeerArchivo(self,archivo):
    with Path(archivo).open(encoding="UTF-8")as fuente:
        dic=json.load(fuente)
        fuente.close()
        return dic
 def DecodificarDiccionario(self,dic):
    if '__class__' not in dic:
        return dic
    else:
        class_name=dic['__class__']
        class_=eval(class_name)
        if(class_name=='ListaPersonal'):
            personal=dic['personal']
            lista=class_()
            for i in range(len(personal)):
                dPersonal=personal[i]
                print(dPersonal)
                class_name=dPersonal.pop('__class__')
                class_=eval(class_name)
                atributos=dPersonal['__atributos__']
                unpersonal=class_(**atributos)
                lista.AgregarPersonal(unpersonal)
        return lista
