class Curso:
    def __init__(self, nombre):
        self.__nombre_atributo_curso = nombre
        self.__nota = 0

    @property
    def nombre(self):
        return self.__nombre_atributo_curso

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nueva_nota):
        self.__nota = nueva_nota