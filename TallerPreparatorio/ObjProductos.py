class Almacen:
    def __init__(self, nombre,precio,cantidad):
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad

    @property
    def nombre(self):
        return self._nombre
    @property
    def precio(self):
        return self._precio
    @property
    def cantidad(self):
        return self._cantidad
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    @precio.setter
    def precio(self, precio):
        self._precio = precio
    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad
