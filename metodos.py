class Metodosmatrices:
    def Crearmatriz(self):
        dimensiones = input("Ingrese las dimensiones de la matriz: ")
        self.filas = dimensiones
        self.columnas = dimensiones
        matriz = [[None for _ in range(self.columnas)] for _ in range(self.filas)]
        self.matriz = matriz

    def Mostrarmatriz(self):
        print(self.matriz)