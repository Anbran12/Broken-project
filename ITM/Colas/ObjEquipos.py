class Computador:
    def __init__(self, serial, marca, mram, dduro, precio, usuario, disponible):
        self.serial = serial
        self.marca = marca
        self.mram = mram
        self.dduro = dduro
        self.precio = precio
        self.disponible = disponible
        self.usuario = usuario

class Tablet:
    def __init__(self, serial, marca, mram, tamano, precio, usuario, disponible):
        self.serial = serial
        self.marca = marca
        self.mram = mram
        self.tamano = tamano
        self.precio = precio
        self.disponible = disponible
        self.usuario = usuario