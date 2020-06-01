from Personal import Personal
from Docente import Docente
from Investigador import Investigador
import json
class DocenteInvestigador(Investigador,Docente):
    __CategoriaIncentivos=''
    __ImporteExtra=0
    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad,carrera,cargo,catedra,areainv,tipoinv,categoriainc,importeExtra):
        super().__init__(cuil,apellido,nombre,sueldobasico,antiguedad,carrera,cargo,catedra,areainv,tipoinv)
        self.__CategoriaIncentivos=categoriainc
        self.__ImporteExtra=importeExtra
    def __str__(self):
        super().__str__()
        cadena='Categoria De Incentivos {}\n'.format(self.__CategoriaIncentivos)
        cadena+='Importe extra docencia e investigacion {}'.format(self.__ImporteExtra)
        return cadena
    def getCategoriaIncentivos(self):
        return self.__CategoriaIncentivos
    def getImporteExtra(self):
        return self.__ImporteExtra
    def toJson(self):
        dic=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=self.getCuil(),
                apellido=self.getApellido(),
                nombre=self.getNombre(),
                sueldobasico=self.getSueldoBasico(),
                antiguedad=self.getAntiguedad(),
                carrera=self.getCarrera(),
                cargo=self.getCargo(),
                catedra=self.getCatedra(),
                areainv=self.getArea(),
                tipoinv=self.getTipo(),
                categoriainc=self.__CategoriaIncentivos,
                importeExtra=self.__ImporteExtra
            )
        )
        return dic    
