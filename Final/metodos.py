import Objproductos as ObjP
import ObjLibreria as ObjL

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
        ObjLibreria = MetodosMatrices()
        ObjLibreria.Crearmatriz()
        for i in range(ObjLibreria.dimensiones):
            for j in range(ObjLibreria.dimensiones):
                ObjLibreria.matriz[i][j] = ObjL.Libreria(input("Ingrese el titulo del libro: "), input("Ingrese el autor del libro: "), int(input("Ingrese el precio del libro: ")))
        self.matriz = ObjLibreria.matriz

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
