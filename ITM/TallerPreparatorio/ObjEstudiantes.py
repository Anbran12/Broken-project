class Estudiantes:
    def __init__(self, nombre, calificacion):
        self._nombre = nombre
        self._calificacion = calificacion

    @property
    def nombre(self):
        return self._nombre
    @property
    def calificacion(self):
        return self._calificacion
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    @calificacion.setter
    def calificacion(self, calificacion):
        self._calificacion = calificacion
