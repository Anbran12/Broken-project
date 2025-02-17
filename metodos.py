#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# METODOS DE MATRICES

class Metodosmatrices:
    def Crearmatriz(self):
        dimensiones = int(input("Ingrese las dimensiones de la matriz: "))
        self.dimensiones = dimensiones
        matriz = [[None for _ in range(self.dimensiones)] for _ in range(self.dimensiones)]
        self.matriz = matriz

class almacen:
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

class personas:
    def llenarmatriz(self):
        obj = Metodosmatrices()
        obj.Crearmatriz()
        for i in range(obj.dimensiones):
            for j in range(obj.dimensiones):
                obj.matriz[i][j] = almacen(input("Ingrese el nombre del producto: "), int(input("Ingrese el precio del producto: ")), int(input("Ingrese la cantidad del producto: ")))
        self.matriz = obj.matriz

    def Mostrarmatriz(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                print(f"Nombre: {self.matriz[i][j].get_nombre()} \nPrecio: {self.matriz[i][j].get_precio()} \nCantidad: {self.matriz[i][j].get_cantidad()}\n\n")        

    def Buscarproducto(self):
        producto = input("Ingrese el nombre del producto a buscar: ")
        for i in range (len(self.matriz)):
            for j in range (len(self.matriz)):
                if self.matriz[i][j].get_nombre() == producto:
                    print(f"La ubicación del producto es:\n Fila: {i} \n Columna: {j}\n\n")

    def Contarproductos(self):
        totalproductos = 0
        for i in range (len(self.matriz)):
            for j in range (len(self.matriz)):
                totalproductos += self.matriz[i][j].get_cantidad()
        print(f"El total de productos en el almacen es: {totalproductos}\n\n")



#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# PUNTOS

#class main:
#    def main(self):
#        matrizObj = Metodosmatrices()
#        matrizObj.Crearmatriz()

class punto1:
    def punto1(self):
        obj = personas()
        obj.llenarmatriz()
        obj.Mostrarmatriz()
        obj.Buscarproducto()

class punto2:
    def punto2(self):
        obj = personas()
        obj.llenarmatriz()
        obj.Mostrarmatriz()
        obj.Contarproductos()

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# MENU PRINCIPAL

#MAIN
#main = main()
#print(main.main())

opcion = int(input("Ingrese el punto a ejecutar: "))

if opcion == 1:
    #PUNTO 1
    punto1 = punto1()
    print(punto1.punto1())

if opcion == 2:
    #PUNTO 2
    punto2 = punto2()
    print(punto2.punto2())
