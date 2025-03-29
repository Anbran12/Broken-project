class Pc:
    def __init__(self, serial, marca, precio):
        self._serial = serial
        self._marca = marca
        self._precio = precio

    @property
    def serial(self):
        return self._serial
    @property
    def marca(self):
        return self._marca
    @property
    def precio(self):
        return self._precio
    
    @serial.setter
    def serial(self,serial):
        self._serial = serial
    @marca.setter
    def marca(self,marca):
        self._marca = marca
    @precio.setter
    def precio(self,precio):
        self._precio = precio