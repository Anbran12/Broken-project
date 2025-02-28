class Asiento:
    def __init__(self,numero,fila,precio):
        self._numero = numero
        self._fila = fila
        self._precio = precio

    @property
    def numero(self):
        return self._numero
    @property
    def fila(self):
        return self._fila
    @property
    def precio(self):
        return self._precio
    @numero.setter
    def numero(self,numero):
        self._numero = numero
    @fila.setter
    def fila(self,fila):
        self._fila = fila
    @precio.setter
    def precio(self,precio):
        self._precio = precio
    