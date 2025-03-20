class Honda:
    def __init__(self, marca, referencia, cantidad, precio):
        self._marca = marca
        self._referencia = referencia
        self._cantidad = cantidad
        self._precio = precio
    
    @property
    def marca(self):
        return self._marca
    @property
    def referencia(self):
        return self._referencia
    @property
    def cantidad(self):
        return self._cantidad
    @property
    def precio(self):
        return self._precio
    @marca.setter
    def marca(self,marca):
        self._marca = marca
    @referencia.setter
    def referencia(self,referencia):
        self._referencia = referencia
    @cantidad.setter
    def cantidad(self,cantidad):
        self._cantidad = cantidad
    @precio.setter
    def precio(self,precio):
        self._precio = precio
    