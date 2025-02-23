class Almacen2:
    def __init__(self, nombre,precio,disponible):
        self.__nombre = nombre
        self.__precio = precio
        self.__disponible = disponible

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_precio(self, precio):
        self.__precio = precio

    def set_disponible(self, disponible):
        self.__disponible = disponible

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_disponible(self):
        return self.__disponible
