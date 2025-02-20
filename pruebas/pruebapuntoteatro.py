class MetodosMatrices:
	def CrearMatriz(self):
		dimensiones = int(input("Ingresa las dimensiones de la matriz: "))
		self.dimensiones = dimensiones
		Matriz = [[0 for _ in range(self.dimensiones)]for _ in range (self.dimensiones)]
		self.Matriz = Matriz

	def MostrarMatriz(self):
		for i in range(len(self.Matriz)):
			for j in range(len(self.Matriz)):
				print(f"El asiento es: {self.Matriz[i][j].get_asiento()}\n El número es: {self.Matriz[i][j].get_numero()}\n La fila es: {self.Matriz[i][j].get_fila()} El precio es: {self.Matriz[i][j].get_precio()}")

class Teatro:
	def __init__(self, asiento, numero, fila, precio):
		self.__asiento = asiento
		self.__numero = numero
		self.__fila = fila
		self.__precio = precio

	def get_asiento(self):
		return self.__asiento
	def set_asiento(self, asiento):
		self.__asiento = asiento
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



class PersonasTeatro:
	def LlenarMatrizPT(self):
		for i in range(len(self.Matriz)):
			for j in range(len(self.Matriz)):
				persona = input(f"Ingresa un asiento: {set_asiento} Ingresa el número del asiento: {set_numero} Ingresa el número de la fila: {set_fila} Ingresa el precio: {set_precio}")
				self.Matriz[i][j].append = persona


Obj_matriz = MetodosMatrices()
Obj_matriz.CrearMatriz()
Obj_matriz.MostrarMatriz()
Obj_persona = PersonasTeatro()
Obj_persona.LlenarMatrizPT()
Obj_prueba.MostrarMatriz()