class Almacen2:
    def __init__(self, nombre,precio,disponible):
        self._nombre = nombre
        self._precio = precio
        self._disponible = disponible

    @property
    def nombre(self):
        return self._nombre
    @property
    def precio(self):
        return self._precio
    @property
    def disponible(self):
        return self._disponible
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    @precio.setter
    def precio(self, precio):
        self._precio = precio
    @disponible.setter
    def disponible(self, disponible):
        self._disponible = disponible
