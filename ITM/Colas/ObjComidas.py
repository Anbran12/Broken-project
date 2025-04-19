class Comidas:
    def __init__(self, usuario, tipocomida, bebida, precio):
        self._usuario = usuario
        self._tipocomida = tipocomida
        self._bebida = bebida
        self._precio = precio
        
    @property
    def usuario(self):
        return self._usuario
    @property
    def tipocomida(self):
        return self._tipocomida
    @property
    def bebida(self):
        return self._bebida
    @property
    def precio(self):
        return self._precio
    
    @usuario.setter
    def usuario(self,usuario):
        self._usuario = usuario
    @tipocomida.setter
    def tipocomida(self,tipocomida):
        self._tipocomida = tipocomida
    @bebida.setter
    def bebida(self,bebida):
        self._bebida = bebida
    @precio.setter
    def precio(self,precio):
        self._precio = precio