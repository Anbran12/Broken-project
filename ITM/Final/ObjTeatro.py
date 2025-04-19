class Asiento:
	def __init__(self, numero, fila, precio):
		self.__numero = numero
		self.__fila = fila
		self.__precio = precio
	def get_numero(self):
		return self.__numero
	def set_numero(self, numero):
		self.__numero = numero
	def get_fila(self):
		return self.__fila
	def set_fila(self, fila):
		self.__fila = fila
	def get_precio(self):
		return self.__precio
	def set_precio(self, precio):
		self.__precio = precio