import ObjProductos as Obj1
import ObjProductos2 as Obj2
import ObjAsiento as Obj3
import ObjEstudiantes as Obj4

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
        Mdisponible = [[None for filas in range(Dim)]for columna in range(Dim)]
        self.mdisponible = Mdisponible


    def mostrarmatrizff(self):
        for i in range(len(self.matriz)):
            print(self.matriz[i])


    def ingresarproductos(self):
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
                print(f"\nProducto: {self.matriz[i][j].nombre}\nPrecio: {self.matriz[i][j].precio}\nCantidad: {self.matriz[i][j].cantidad}")

        
    def buscarproducto(self):
        buscar = ""
        while buscar == "":
            try:
                buscar = input("\n- Ingresa el nombre del producto a buscar: ")
            except ValueError:
                print("\nEl valor ingresado no es valido.")
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                if self.matriz[i][j].nombre == buscar:
                    print(f"\nEl producto {buscar}, se encuentra en la siguiente posición: \nFila: {i}\nColumna: {j}")
        
    def totalproductos(self):
        suma = 0
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                suma += self.matriz[i][j].cantidad
        print(f"\nEl total de productos en la tienda es: {suma}")


    def llenarmatrizpd(self):
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
                        D = input("\n- Ingresa la disponibilidad (0/1): ")
                        if D == "0":
                            D = False
                        elif D == "1":
                            D = True
                        else:
                            D = None
                            print("\nEl valor ingresado no es valido.")
                    except ValueError:
                        print("\nEl valor ingresado no es valido.")              
                self.matriz[i][j] = Obj2.Almacen2(N,P,D)

    def productosdisponibles(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                if self.matriz[i][j].disponible == True: 
                    self.mdisponible[i][j] = self.matriz[i][j]

    def mostrarmatrizpd(self):
        print("\nProductos disponibles:\n")
        for i in range(len(self.mdisponible)):
            for j in range(len(self.mdisponible)):
                if self.mdisponible[i][j] != None:
                    print(f"\nProducto: {self.mdisponible[i][j].nombre}\nPrecio: {self.mdisponible[i][j].precio}\nDisponibilidad: {self.mdisponible[i][j].disponible}")
                    
    def llenarmatrizteatro(self):
        for i in range(len(self.matriz)):
            for j in range (len(self.matriz)):
                N,F,P = 0,0,0
                while N == 0:
                    try:
                        N = int(input("Ingresa el número del asiento: "))
                    except ValueError:
                        print("El valor ingresado no es valido.")
                        
                while F == 0:
                    try:
                        F = int(input("Ingresa la fila del asiento: "))
                    except ValueError:
                        print("El valor ingresado no es valido.")
                        
                while P == 0:
                    try:
                        P = int(input("Ingresa el precio del asiento: "))
                    except ValueError:
                        print("El valor ingresado no es valido.")
                self.matriz[i][j] = Obj3.Asiento(N,F,P)
                
    def mostrarmatrizteatro(self):
        print("\nAsientos disponibles: ")
        for i in range(len(self.matriz)):
            for j in range (len(self.matriz)):
                print(f"Número: {self.matriz[i][j].numero}\nFila: {self.matriz[i][j].fila}\nPrecio: {self.matriz[i][j].precio}")
                
    def ordenarfilasteatro(self):
        for i in range(len(self.matriz)):
            for j in range (len(self.matriz)):
                V1 = self.matriz[i][j].precio
                for k in range(len(self.matriz)):
                    for l in range (len(self.matriz)):
                        V2 = self.matriz[k][l].precio
                        Temp1 = self.matriz[i][j]
                        Temp2 = self.matriz[k][l]
                        if V1 > V2:
                            self.matriz[i][j] = Temp2
                            self.matriz[j][k] = Temp1

    def llenarmatrizestudiantes(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                N,C = "",0.0
                while N == "":
                    try:
                        N = input("\nIngresa el nombre del estudiante: ")
                    except ValueError:
                        print("\nEl valor ingresado no es valido.")
                    try:
                        C = input("\nIngresa el la calificacion 1: ")
                    except ValueError:
                        print("\nEl valor ingresado no es valido.")
                self.matriz[i][j] = Obj4.Estudiantes(N,C)
    
    def mostrarmatrizestudiantes(self):
        print("\nEstudiantes registrados: ")
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                print(f"\nNombre: {self.matriz[i][j].nombre}\nCalificación: {self.matriz[i][j].calificacion}")

    def distribucionestudiantes(self):
        calificacionA = [[None for i in range(self.Dim)]for j in range(self.Dim)]
        calificacionB = [[None for i in range(self.Dim)]for j in range(self.Dim)]
        calificacionC = [[None for i in range(self.Dim)]for j in range(self.Dim)]
        contador1,contador2,contador3 = 0,0,0
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                variable = self.matriz[i][j].calificacion
                if variable.lower() == "a":
                    calificacionA.append(self.matriz[i][j])
                else:
                    if variable.lower() == "b":
                        calificacionB.append(self.matriz[i][j])
                    else:
                        if variable.lower() == "c":
                            calificacionC.append(self.matriz[i][j])

        print("\nEstudiantes calificación A: ")
        for i in range(len(calificacionA)):
            for j in range(len(calificacionA)):
                print(f"\nNombre: {calificacionA[i][j].nombre}\nCalificación: {calificacionA[i][j].calificacion}")

        print("\nEstudiantes calificación B: ")
        for i in range(len(calificacionA)):
            for j in range(len(calificacionA)):
                print(f"\nNombre: {calificacionB[i][j].nombre}\nCalificación: {calificacionB[i][j].calificacion}")

        print("\nEstudiantes calificación C: ")
        for i in range(len(calificacionA)):
            for j in range(len(calificacionA)):
                print(f"\nNombre: {calificacionC[i][j].nombre}\nCalificación: {calificacionC[i][j].calificacion}")
