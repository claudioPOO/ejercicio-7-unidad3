from Personal import Personal
import json
class Docente(Personal):
    __Carrera=''
    __Cargo=''
    __Catedra=''
    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad,carrera,cargo,catedra,areainv='',tipoinv=''):
        super().__init__(cuil,apellido,nombre,sueldobasico,antiguedad,carrera,cargo,catedra,areainv,tipoinv)
        self.__Carrera=carrera
        self.__Cargo=cargo
        self.__Catedra=catedra
    def __str__(self):
        super().__str__()
        cadena='Carrera {} Cargo {} Catedra {}'.format(self.__Carrera,self.__Cargo,self.__Catedra)
        return cadena
    def getCarrera(self):
        return self.__Carrera
    def getCargo(self):
        return self.__Cargo
    def getCatedra(self):
        return self.__Catedra            
    def toJson(self):
        dic=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=self.getCuil(),
                apellido=self.getApellido(),
                nombre=self.getNombre(),
                sueldobasico=self.getSueldoBasico(),
                antiguedad=self.getAntiguedad(),
                carrera=self.__Carrera,
                cargo=self.__Cargo,
                catedra=self.__Catedra(),
            )
        )
        return dic        
                
