class Pc:
    def __init__(self, serial, marca, mram, dduro, precio, disponible):
        self._serial = serial
        self._marca = marca
        self._mram = mram
        self._dduro = dduro
        self._precio = precio
        self._disponible = disponible

    @property
    def serial(self):
        return self._serial
    @property
    def marca(self):
        return self._marca
    @property
    def mram(self):
        return self._mram
    @property
    def dduro(self):
        return self._dduro
    @property
    def precio(self):
        return self._precio
    @property
    def disponible(self):
        return self._disponible

    @serial.setter
    def serial(self,serial):
        self._serial = serial
    @marca.setter
    def marca(self,marca):
        self._marca = marca
    @mram.setter
    def mram(self,mram):
        self._mram = mram
    @dduro.setter
    def dduro(self,dduro):
        self._dduro = dduro
    @precio.setter
    def precio(self,precio):
        self._precio = precio
    @disponible.setter
    def disponible(self,disponible):
        self._disponible = disponible

class Tablet:
    def __init__(self, serial, marca, mram, tamano, precio, disponible):
        self._serial = serial
        self._marca = marca
        self._mram = mram
        self._tamano = tamano
        self._precio = precio
        self._disponible = disponible

    @property
    def serial(self):
        return self._serial
    @property
    def marca(self):
        return self._marca
    @property
    def mram(self):
        return self._mram
    @property
    def tamano(self):
        return self._tamano
    @property
    def precio(self):
        return self._precio
    @property
    def disponible(self):
        return self._disponible

    @serial.setter
    def serial(self,serial):
        self._serial = serial
    @marca.setter
    def marca(self,marca):
        self._marca = marca
    @mram.setter
    def mram(self,mram):
        self._mram = mram
    @tamano.setter
    def tamano(self,tamano):
        self._tamano = tamano
    @precio.setter
    def precio(self,precio):
        self._precio = precio
    @disponible.setter
    def disponible(self,disponible):
        self._disponible = disponible

class Estudiantes:
    def __init__(self, serial, nomestudiante, carnet):
        self._serial = serial
        self._nomestudiante = nomestudiante
        self._carnet = carnet

    @property
    def serial(self):
        return self._serial
    @property
    def nomestudiante(self):
        return self._nomestudiante
    @property
    def carnet(self):
        return self._carnet

    @serial.setter
    def serial(self,serial):
        self._serial = serial
    @nomestudiante.setter
    def nomestudiante(self,nomestudiante):
        self._nomestudiante = nomestudiante
    @carnet.setter
    def carnet(self,carnet):
        self._carnet = carnet

# Serial,Marca,MRam,Dduro,Precio,Disponible
# Serial,Marca,MRam,Tamano,Precio,Disponible
# Serial,NomEstudiante,Carnet