import random

class Metodos:
    def crearmatriz(self):
        dimensiones = int(input("\nIngresa el la dimensión de la matriz: "))
        self.dimensiones = dimensiones
        print("\nIngresar rango de valores para matriz: ")
        Vmin, Vmax = int(input("Valor mínimo: ")), int(input("Valor máximo: "))
        matriz = [[random.randint(Vmin,Vmax) for filas in range(dimensiones)]for columnas in range(dimensiones)]
        self.matriz = matriz

    def mostrarmatriz(self):
        for i in range(len(self.matriz)):
#Al hacer uso de este línea se imprimen los dígitos uno bajo otro, si no esta activa se expone la lista completa conservando la estructura de matriz.
#            for j in range(len(self.matriz)):
            print(f"\n{self.matriz[i]}")

    def sumamatriz(self):
        S = 0
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                S += self.matriz[i][j]
        print(f"La suma de la matriz es: {S}")

    def numeromayor(self):
        Nmayor = 0
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                if self.matriz[i][j] > Nmayor:
                    Nmayor = self.matriz[i][j]
        print(f"\nEl número mayor es: {Nmayor}")

    def sumasporfyc(self):

        for i in range(len(self.matriz)):
            Sumafilas = 0
            Sumacolumnas = 0
            for j in range(len(self.matriz)):
                Sumafilas += self.matriz[i][j]
                Sumacolumnas += self.matriz[j][i]
            print(f"\nSuma fila {i}: {Sumafilas}")
            print(f"\nSuma columna {i}: {Sumacolumnas}")

    def mayorsumacolumna(self):
        Msuma = 0
        Ubi = 0
        for i in range(len(self.matriz)):
            Sumacolumnas = 0
            for j in range(len(self.matriz)):
                Sumacolumnas += self.matriz[j][i]
            if Sumacolumnas > Msuma:
                Msuma = Sumacolumnas
                Ubi = j
        print(f"\nLa columna con mayor suma es la {Ubi}, con un total: {Msuma}")

    def matrizenvector(self):
        V = []
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                V.append(self.matriz[i][j])
        print(f"\nLa matriz almacenada en vector: {V}")


    def sumadefycenvector(self):
        suma = []
        for i in range(len(self.matriz)):
            Sumafilas = 0
            Sumacolumnas = 0
            for j in range(len(self.matriz)):
                Sumafilas += self.matriz[i][j]
                Sumacolumnas += self.matriz[j][i]
            suma.append(Sumafilas)
            suma.append(Sumacolumnas)
        print(f"\nSuma filas y columnas en vector: {suma}")
    
    def positivosynegativos(self):
        P,N,C = 0,0,0

        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                if self.matriz[i][j] == 0:
                    C += 1
                elif self.matriz[i][j] > 0:
                    P += 1
                elif self.matriz[i][j] < 0:
                    N += 1
        print(f"\nTotal:\nNúmeros positivos: {P}\nNúmeros negativos: {N}\nValores igual a cero: {C}")

