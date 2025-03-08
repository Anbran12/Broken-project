class Vehiculo:
    def __init__(self,marca,color,precio):
        self._marca = marca
        self._color = color
        self._precio = precio
        
    @property
    def marca(self):
        return self._marca

    @property
    def color(self):
        return self._color
    
    @property
    def precio(self):
        return self._precio
    @marca.setter
    def marca(self,marca):
        self._marca = marca
        
    @color.setter
    def color(self,color):
        self._color = color
        
    @precio.setter
    def precio(self,precio):
        self._precio = precio