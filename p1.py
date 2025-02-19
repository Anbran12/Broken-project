class MetodosMatrices:
    def CrearMatriz(self):
        dimensiones = int(input("Ingresa las dimensiones de la matriz: "))
        self.dimensiones = dimensiones
        Matriz = [[0 for _ in range(self.dimensiones)]for _ in range (self.dimensiones)]
        self.Matriz = Matriz

    def MostrarMatriz(self):
        for i in len(self.Matriz):
            for j in len(self.Matriz):
                return self.Matriz[i][j]

    def LlenarMatriz(self):
        for i in len(self.Matriz):
            for j in len(self.Matriz):
                dato = input("Ingresa un dato: ")
                self.Matriz[i][j] = dato


Obj_prueba = MetodosMatrices()
Obj_prueba = CrearMatriz()
Obj_prueba = Mostrarmatriz()
Obj_prueba = LlenarMatriz()