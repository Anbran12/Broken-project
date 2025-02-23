import ObjProductos as Obj1
import ObjProductos2 as Obj2

class Metodos:
    def crearmatriz(self):
        Dim = 0
        while Dim == 0:
            try:
                Dim = int(input("\nIngresa la dimensión de la matriz: "))
            except ValueError:
                print("\nEl valor ingresado debe ser un número entero.")
        self.Dim = Dim
        matriz = [[None for filas in range(Dim)]for columna in range(Dim)]
        self.matriz = matriz

    def mostrarmatrizff(self):
        for i in range(len(self.matriz)):
            print(self.matriz[i])


    def ingresarproductos(self):
        M = Metodos()
        M.crearmatriz()
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                N,P,C = "",0,0
                while N == "":
                    try:
                        N = input("\n- Ingresa el nombre del producto: ")
                    except ValueError:
                        print("\nEl valor ingresado no es valido.")
                while P == 0:
                    try:
                        P = float(input("\n- Ingresa el precio: "))
                    except ValueError:
                        print("\nEl valor ingresado no es valido.")
                while C == 0:
                    try:
                        C = int(input("\n- Ingresa la cantidad: "))
                    except ValueError:
                        print("\nEl valor ingresado no es valido.")              
                self.matriz[i][j] = Obj1.Almacen(N,P,C)
                

    def mostrarproductos(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                print(f"\nProducto: {self.matriz[i][j].get_nombre()}\nPrecio: {self.matriz[i][j].get_precio()}\nCantidad: {self.matriz[i][j].get_cantidad()}")

        
    def buscarproducto(self):
        buscar = ""
        while buscar == "":
            try:
                buscar = input("\n- Ingresa el nombre del producto a buscar: ")
            except ValueError:
                print("\nEl valor ingresado no es valido.")
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                if self.matriz[i][j].get_nombre() == buscar:
                    print(f"\nEl producto {buscar}, se encuentra en la siguiente posición: \nFila: {i}\nColumna: {j}")
        
    def totalproductos(self):
        suma = 0
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                suma += self.matriz[i][j].get_cantidad()
        print(f"\nEl total de productos en la tienda es: {suma}")


    def llenarmatrizpd(self):
        M = Metodos()
        M.crearmatriz()
        self.mdisponible = self.matriz
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                N,P,D = "",0,None
                while N == "":
                    try:
                        N = input("\n- Ingresa el nombre del producto: ")
                    except ValueError:
                        print("\nEl valor ingresado no es valido.")
                while P == 0:
                    try:
                        P = float(input("\n- Ingresa el precio: "))
                    except ValueError:
                        print("\nEl valor ingresado no es valido.")
                while D == None:
                    try:
                        D= bool(input("\n- Ingresa la disponibilidad (False/True): "))
                    except ValueError:
                        print("\nEl valor ingresado no es valido.")              
                self.matriz[i][j] = Obj2.Almacen2(N,P,D)

    def productosdisponibles(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                if self.matriz[i][j].get_disponible == True: 
                    self.mdisponible[i][j] = self.matriz[i][j]

    def mostrarmatrizpd(self):
        for i in range(len(self.mdisponible)):
            for j in range(len(self.mdisponible)):
                if self.mdisponible[i][j] != None:
                    print(f"\nProducto: {self.mdisponible[i][j].get_nombre()}\nPrecio: {self.mdisponible[i][j].get_precio()}\nDisponibilidad: {self.mdisponible[i][j].get_disponible()}")