import ObjProductos as ObjP
import ObjLibreria as ObjL
import ObjTeatro as ObjT

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# METODOS DE MATRICES

class MetodosMatrices:
    def Crearmatriz(self):
        dimensiones = int(input("Ingrese las dimensiones de la matriz: "))
        self.dimensiones = dimensiones
        matriz = [[None for _ in range(self.dimensiones)] for _ in range(self.dimensiones)]
        self.matriz = matriz

class ProductosAlmacen:
    def llenarmatriz(self):
        obj = MetodosMatrices()
        obj.Crearmatriz()
        for i in range(obj.dimensiones):
            for j in range(obj.dimensiones):
                obj.matriz[i][j] = ObjP.Almacen(input("Ingrese el nombre del producto: "), int(input("Ingrese el precio del producto: ")), int(input("Ingrese la cantidad del producto: ")))
                print("\n")
        self.matriz = obj.matriz

    def MostrarMatrizAlmacen(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                print(f"Nombre: {self.matriz[i][j].get_nombre()} \nPrecio: {self.matriz[i][j].get_precio()} \nCantidad: {self.matriz[i][j].get_cantidad()}\n\n")        

    def Buscarproducto(self):
        producto = input("Ingrese el nombre del producto a buscar: ")
        for i in range (len(self.matriz)):
            for j in range (len(self.matriz)):
                if self.matriz[i][j].get_nombre() == producto:
                    print(f"\nLa ubicación del producto es:\nFila: {i} \nColumna: {j}\n\n")

    def ContarProductosAlmacen(self):
        totalProductosAlmacen = 0
        for i in range (len(self.matriz)):
            for j in range (len(self.matriz)):
                totalProductosAlmacen += self.matriz[i][j].get_cantidad()
        print(f"\nEl total de ProductosAlmacen en el Almacen es: {totalProductosAlmacen}\n\n")

class MetodosLibreria:
    def LlenarMatriz(self):
        ObjLibro = MetodosMatrices()
        ObjLibro.Crearmatriz()
        for i in range(ObjLibro.dimensiones):
            for j in range(ObjLibro.dimensiones):
                ObjLibro.matriz[i][j] = ObjL.Libreria(input("Ingrese el titulo del libro: "), input("Ingrese el autor del libro: "), int(input("Ingrese el precio del libro: ")))
        self.matriz = ObjLibro.matriz

    def MostrarMatrizLibreria(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                print(f"Titulo: {self.matriz[i][j].get_titulo()} \nAutor: {self.matriz[i][j].get_autor()} \nPrecio: {self.matriz[i][j].get_precio()}\n\n")

    def ValorLibro(self):
        Vlibro = 0
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                if self.matriz[i][j].get_precio() > Vlibro:
                    Vlibro = self.matriz[i][j].get_precio()
        print(f"El libro más caro tiene un valor de: {Vlibro}\n\n")

class PersonasTeatro:

    def LlenarMatrizPT(self):
        ObjTeatro1 = MetodosMatrices()
        ObjTeatro1.Crearmatriz()
        for i in range(ObjTeatro1.dimensiones):
            for j in range(ObjTeatro1.dimensiones):
                ObjTeatro1.matriz[i][j] = ObjT.Asiento(int(input("\nIngresa el número de asiento: ")), int(input("Ingresa el número de fila: ")), int(input("Ingresa el precio: ")))
        self.matriz = ObjTeatro1.matriz

    def MostrarMatrizPT(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                print(f"\nEl número de asiento es: {self.matriz[i][j].get_numero()}\nEl número de fila es: {self.matriz[i][j].get_fila()}\nEl precio es: {self.matriz[i][j].get_precio()}")

    def OrdenarPorPrecio(self):
        Ordenada = [sorted(fila, key=lambda p: p.get_precio()) for fila in self.matriz]
        for fila in Ordenada:
                print(fila)

        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                print(f"\nEl número de asiento es: {Ordenada[i][j].get_numero()}\nEl número de fila es: {Ordenada[i][j].get_fila()}\nEl precio es: {Ordenada[i][j].get_precio()}")