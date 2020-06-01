from Personal import Personal
import json
class Investigador(Personal):
    __AreaInv=''
    __TipoInv=''
    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad,areainv,tipoinv,carrera='',cargo='',catedra=''):
        super().__init__(cuil,apellido,nombre,sueldobasico,antiguedad,carrera,cargo,catedra,areainv,tipoinv)
        self.__AreaInv=areainv
        self.__TipoInv=tipoinv
    def __str__(self):
        super().__str__()
        cadena='Area {} Tipo {}'.format(self.__AreaInv,self.__TipoInv)
        return cadena
    def getArea(self):
        return self.__AreaInv
    def getTipo(self):
        return self.__TipoInv
    def toJson(self):
        dic=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=self.getCuil(),
                apellido=self.getApellido(),
                nombre=self.getNombre(),
                sueldobasico=self.getSueldoBasico(),
                antiguedad=self.getAntiguedad(),
                areainv=self.__AreaInv,
                tipoinv=self.__TipoInv
            )
        )
        return dic                        