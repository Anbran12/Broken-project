#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# METODOS DE MATRICES

class MetodosMatrices:
    def Crearmatriz(self):
        dimensiones = int(input("Ingrese las dimensiones de la matriz: "))
        self.dimensiones = dimensiones
        matriz = [[None for _ in range(self.dimensiones)] for _ in range(self.dimensiones)]
        self.matriz = matriz

class Almacen:
    def __init__(self, nombre, precio, cantidad):
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad = cantidad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio
        
    def get_cantidad(self):
        return self.__cantidad
 
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

class ProductosAlmacen:
    def llenarmatriz(self):
        obj = MetodosMatrices()
        obj.Crearmatriz()
        for i in range(obj.dimensiones):
            for j in range(obj.dimensiones):
                obj.matriz[i][j] = Almacen(input("Ingrese el nombre del producto: "), int(input("Ingrese el precio del producto: ")), int(input("Ingrese la cantidad del producto: ")))
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
                    print(f"La ubicación del producto es:\n Fila: {i} \n Columna: {j}\n\n")

    def ContarProductosAlmacen(self):
        totalProductosAlmacen = 0
        for i in range (len(self.matriz)):
            for j in range (len(self.matriz)):
                totalProductosAlmacen += self.matriz[i][j].get_cantidad()
        print(f"El total de ProductosAlmacen en el Almacen es: {totalProductosAlmacen}\n\n")

class Libreria:
    def __init__(self, titulo, autor, precio):
        self.__titulo = titulo
        self.__autor = autor
        self.__precio = precio

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_autor(self):
        return self.__autor

    def set_autor(self, autor):
        self.__autor = autor
        
    def get_precio(self):
        return self.__precio
 
    def set_precio(self, precio):
        self.__precio = precio

class MetodosLibreria:
    def LlenarMatriz(self):
        ObjLibreria = MetodosMatrices()
        ObjLibreria.Crearmatriz()
        for i in range(ObjLibreria.dimensiones):
            for j in range(ObjLibreria.dimensiones):
                ObjLibreria.matriz[i][j] = Libreria(input("Ingrese el titulo del libro: "), input("Ingrese el autor del libro: "), int(input("Ingrese el precio del libro: ")))
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

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# PUNTOS

#class Main:
#    def main(self):
#        matrizObj = MetodosMatrices()
#        matrizObj.Crearmatriz()

class Punto1:
    def Epunto1(self):
        obj = ProductosAlmacen()
        obj.llenarmatriz()
        obj.MostrarMatrizAlmacen()
        obj.Buscarproducto()

class Punto2:
    def Epunto2(self):
        obj = ProductosAlmacen()
        obj.llenarmatriz()
        obj.MostrarMatrizAlmacen()
        obj.ContarProductosAlmacen()

class Punto3:
    def Epunto3(self):
        obj = MetodosLibreria()
        obj.LlenarMatriz()
        obj.MostrarMatrizLibreria()
        obj.ValorLibro()

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# MENU PRINCIPAL

#MAIN
#main = main()
#print(main.main())

opcion = int(input("Ingrese el punto a ejecutar: "))

if opcion == 1:
    #PUNTO 1
    punto1 = Punto1()
    print(punto1.Epunto1())

if opcion == 2:
    #PUNTO 2
    punto2 = Punto2()
    print(punto2.Epunto2())

if opcion == 3:
    #PUNTO 3
    punto3 = Punto3()
    print(punto3.Epunto3())