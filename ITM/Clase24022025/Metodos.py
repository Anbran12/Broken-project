import ObjProducto as ObjP
class Metodos:

# Necesario validar como recorrer matrices que tienen diferentes dimensiones, ya que si se tienen menos cantidad de columnas finaliza el recorrido y no realiza validación de las filas faltantes.
    def llenarmatriz(self):
        filas = int(input("Ingresa la dimensión de las filas: "))
        columnas = int(input("ingresa la dimensión de las columnas: "))
        matriz = [[None for fila in range(filas)]for columna in range(columnas)]
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                N,P,S = "",0,0
                N = input("Ingresa el nombre del producto: ")
                P = int(input("Ingresa el precio: "))
                S = int(input("Ingresa el stock: "))
                matriz[i][j] = ObjP.Almacen(N,P,S)
        
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                print(f"\nNombre: {matriz[i][j].get_nombre()}\nPrecio: {matriz[i][j].get_precio()}\nStock: {matriz[i][j].get_stock()}")

    def validarmatrices(self):
            pass
# Validar si la información de las dos matrices contienen productos que coinciden, si estos coinciden se suma el stock y se suma en la matriz 1, lo productos que solo se encuentran en la matriz 2 se pasan a la 1.
        
Obj = Metodos()
Obj.llenarmatriz()