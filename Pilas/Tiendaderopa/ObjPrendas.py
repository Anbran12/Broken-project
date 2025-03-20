class Prendas:
    def __init__(self,marca,referencia,precio,cantidad):
        self._marca = marca
        self._referencia = referencia
        self._precio = precio
        self._cantidad = cantidad
        
    @property
    def marca(self):
        return self._marca
    @property
    def referencia(self):
        return self._referencia
    @property
    def precio(self):
        return self._precio
    @property
    def cantidad(self):
        return self._cantidad
    @marca.setter
    def marca(self,marca):
        self._marca = marca
    @referencia.setter
    def referencia(self,referencia):
        self._referencia = referencia
    @precio.setter
    def precio(self,precio):
        self._precio = precio
    @cantidad.setter
    def cantidad(self,cantidad):
        self._cantidad = cantidad