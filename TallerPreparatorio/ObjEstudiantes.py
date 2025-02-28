class Estudiantes:
    def __init__(self, nombre, nota1, nota2, nota3):
        self._nombre = nombre
        self._nota = nota1
        self._nota = nota2
        self._nota = nota3

    @property
    def nombre(self):
        return self._nombre
    @property
    def nota1(self):
        return self._nota1
    @property
    def nota2(self):
        return self._nota2
    @property
    def nota3(self):
        return self._nota3
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    @nota1.setter
    def nota1(self, nota1):
        self._nota1 = nota1
    @nota2.setter
    def nota2(self, nota2):
        self._nota2 = nota2  
    @nota3.setter
    def nota3(self, nota3):
        self._nota3 = nota3  