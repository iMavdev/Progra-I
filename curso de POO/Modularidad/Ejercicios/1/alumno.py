class Alumno:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__relacioncurso = None
        self.__relacioncurso2 = None
        self.__relacionuniversidad = None

    @property
    def nombre(self):
        return self.__nombre

    @property
    def relacioncurso(self):
        return self.__relacioncurso

    @relacioncurso.setter #.setter sugiere que se puede modificar el valor en algún momento de la propiedad o atributo, en este caso el atributo __relacioncurso.
    def relacioncurso(self, nuevo_curso):
        self.__relacioncurso = nuevo_curso

    @property
    def relacioncurso2(self):
        return self.__relacioncurso2

    @relacioncurso2.setter
    def relacioncurso2(self, nuevo_curso):
        self.__relacioncurso2 = nuevo_curso

    @property
    def relacionuniversidad(self):
        return self.__relacionuniversidad

    @relacionuniversidad.setter
    def relacionuniversidad(self, nueva_universidad):
        self.__relacionuniversidad = nueva_universidad
