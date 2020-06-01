from Personal import Personal
import json 
class PersonalApoyo(Personal):
    __Categoria=''
    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad,categoria):
        super().__init__(cuil,apellido,nombre,sueldobasico,antiguedad)
        self.__Categoria=categoria
    def __str__(self):
        super().__str__()
        print('Categoria {}').format(self.__Categoria)
    def getCategoria(self):
        return self.__Categoria
    def toJson(self):
        dic=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=self.getCuil(),
                apellido=self.getApellido(),
                nombre=self.getNombre(),
                sueldobasico=self.getSueldoBasico(),
                antiguedad=self.getAntiguedad(),
                categoria=self.__Categoria
            )
        )
        return dic
