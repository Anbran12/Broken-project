class Almacen:
    def __init__(self, nombre,precio,cantidad):
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad = cantidad

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_precio(self, precio):
        self.__precio = precio

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_cantidad(self):
        return self.__cantidad