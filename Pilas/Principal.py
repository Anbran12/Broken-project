from collections import deque
import ObjVehiculos as ObjV
import ObjHonda as ObjH

class Pila:
    def crearpilageneral(self):
        P = deque()
        self.P = P
    def llenarpilavehiculos(self):
        Decision = 1
        while Decision == 1:                
            M,C,P = "","",0.0
            print("\nA continuación ingresa los datos del vehiculo: ")
            while M=="":
                try:
                    M = input("\n- Ingresa la marca del vehiculo: ")
                except ValueError:
                    print("Valor no valido")
            while C=="":
                try:
                    C = input("- Ingresa el color del vehiculo: ")
                except ValueError:
                    print("Valor no valido")
            while P==0.0:
                try:
                    P = int(input("- Ingresa el precio del vehiculo: "))
                except ValueError:
                    print("Valor no valido")
                    
            self.P.append(ObjV.Vehiculo(M,C,P))

            Estado = True
            while Estado:
                try:
                    Decision = input("\nDesea ingresar otro registro (Si/No): ")
                    if Decision.lower() in ["si","no"]:
                        if Decision == "si":
                            Decision = 1
                            Estado = False
                        else:
                            Decision = 0
                            Estado = False
                    else:
                        print("\nValor no se encuentra dentro de las opciones.")
                except ValueError:
                    print("\nValor no se encuentra dentro de las opciones.")


         
    def mostrarregistrosvehiculos(self):
        for i in self.P:
            print(
                "\n--------------------------------\n",
                f"\nMarca: {i.marca}\nColor: {i.color}\nPrecio: {i.precio}"
                )


    def eliminarregistrovehiculos(self):
        estado = True
        temp = deque()
        self.temp = temp
        while estado:
            try:
                D = input("\nIngresa un dato a eliminar: ")
                while len(self.P):
                    if D == self.P[-1].marca:
                        self.P.pop()
                    else:
                        self.temp.append(self.P.pop())
                while len(self.temp):
                    self.P.append(self.temp.pop())
                estado = False
            except ValueError:
                print("Valor no valido")

    def modificarobjeto(self):
        estado4 = True
        while estado4:
            try:
                opcion1 = input("\n¿Qué vehículo desea modificar: ")
                for vehículos in self.P:
                    if opcion1 == vehículos.marca:
                        opcion2 = int(input("\n¿Qué dato desea modificar (1. Marca, 2. Color 3. Precio): "))
                        if opcion2 == 1:
                            print(f"\nLa marca actual es: {vehículos.marca}")
                            vehículos.marca = input("Ingresa la nueva marca para el vehículo: ")
                            estado4 = False
                        elif opcion2 == 2:
                            print(f"\nEl color actual es: {vehículos.color}")
                            vehículos.color = input("Ingresa el nuevo color para el vehículo: ")
                            estado4 = False
                        elif opcion2 == 3:
                            print(f"\nEl precio actual es: {vehículos.precio}")
                            vehículos.precio = int(input("Ingresa el nuevo precio para el vehículo: "))
                            estado4 = False
#                else:
#                    print("\nEl vehículo no registra.")
            except ValueError:
                print("\nValor no valido o el vehículo no exite.")
# ---------------------------------------------------------------------------------------

    def crearyllenarpilap3(self):
        P = deque()
        self.P = P
        Temp = deque()
        estado = True
        while estado:
            estado2 = True
            while estado2:
                try:
                    numero = int(input("\nIngresa un número entre: "))
                    if numero != 0:
                        estado2 = False
                except ValueError:
                    print("Valor no valido.")
            estado3 = True
            while estado3:
                self.P.append(numero)
                try:
                    E = input("\nDesea ingresar otro numero S/N: ")
                    if E.lower() == "n":
                        estado = False
                        estado2 = False
                        estado3 = False
                    if E.lower() == "s":
                        estado3 = False
                except ValueError:
                    print("Valor no valido.")
        
        while len(self.P):
            Ntemp = self.P.pop()
            if Ntemp < 0:
                Ntemp = 0
                Temp.append(Ntemp)
            elif Ntemp > 7 and Ntemp < 21:
                Ntemp = 50
                Temp.append(Ntemp)
            elif Ntemp > 59 and Ntemp < 63:
                Ntemp = 100
                Temp.append(Ntemp)            
            else:
                Temp.append(Ntemp)
        while len(Temp):
            self.P.append(Temp.pop())
                
    def mostrarpilap3(self):
        for i in self.P:
            print(i)
            
class VHonda:
    def crearpila(self):
        H = deque()
        Temp = deque()
        self.H = H
        self.Temp = Temp
        
    def ingresarrepuestos(self):
        estado = True
        while estado:
            print("\nA continuación ingresa los datos del vehiculo: ")
            M,R,C,P,Otro = "","",-1,0.0,"Pen"
            while M == "":
                try:
                    M = input("Ingresa el nombre del repuesto: ")
                except ValueError:
                    print("Valor no valido.")
            while R == "":
                try:
                    R = input("Ingresa la referencia: ")
                except ValueError:
                    print("Valor no valido.")
            while C == -1:
                try:
                    C = int(input("Ingresa la cantidad: "))
                except ValueError:
                    print("Valor no valido.")
            while P == 0.0:
                try:
                    P = input("Ingresa el precio: ")
                except ValueError:
                    print("Valor no valido.")
            while Otro == "Pen":
                try:
                    Otro = input("Desea ingresar otro producto (S/N): ")
                except ValueError:
                    print("Valor no valido.")
                if "n" == Otro.lower():
                    break
            self.H.append(ObjH.Honda(M,R,C,P)) 
        
    def buscarrepuesto(self):
        buscar = ""
        while buscar == "":
            try:
                buscar = input("\nIngresa el repuesto a buscar: ")
            except ValueError:
                print("Valor no valido.")
                
        for repuesto in self.H:
            if repuesto == buscar:
                print(f"\nLa información del repuesto buscado es: \n- Marca: {repuesto.marca}\n- Referencia: {repuesto.referencia}\n- Cantidad: {repuesto.cantidad}\n- Precio: {repuesto.precio}")
    
    def modificarinformacion(self):
        Modificar = ""
        while Modificar == "":
            try:
                Modificar = input("\nIngresa el repuesto a modificar: ")
            except ValueError:
                print("Valor no valido.")
                
        for repuesto in self.H:
            if repuesto == Modificar:
                print("\n¿Qué dato desea modificar?\n1. Marca\n2. Referencia\n3. Cantidad\n1. Precio")
                opcion = 0
                while opcion == 0:
                    try:
                        opcion = int(input("\nIngresa la opción: "))                    
                    except ValueError:
                        print("Valor no valido.")
                if opcion == 1:
                    cambio = ""
                    while cambio == "":
                        try:
                            cambio = int(input("\nIngresa el nuevo valor:"))
                            repuesto.marca = cambio                    
                        except ValueError:
                            print("Valor no valido.")
                if opcion == 2:
                    cambio = ""
                    while opcion == "":
                        try:
                            cambio = int(input("\nIngresa el nuevo valor:"))
                            repuesto.referencia = cambio                    
                        except ValueError:
                            print("Valor no valido.")
                if opcion == 3:
                    cambio = -1
                    while opcion == -1:
                        try:
                            cambio = int(input("\nIngresa el nuevo valor:"))
                            repuesto.cantidad = cambio                    
                        except ValueError:
                            print("Valor no valido.")
                if opcion == 4:
                    cambio = 0.0
                    while opcion == 0.0:
                        try:
                            cambio = int(input("\nIngresa el nuevo valor:"))
                            repuesto.precio = cambio                    
                        except ValueError:
                            print("Valor no valido.")
                            
    def ventarepuesto(self):
        VModificar = ""
        while VModificar == "":
            try:
                VModificar = input("\nIngresa el repuesto a vender: ")
            except ValueError:
                print("Valor no valido.")
        for repuesto in self.H:
            if repuesto == VModificar:
                print(f"\nEl stock actual de repuesto {repuesto.marca} es {repuesto.cantidad}")
        Estado3 = True
        while Estado3:
            try:
                CModificar = int(input("\nIngresa la cantidad a vender: "))
            except ValueError:
                print("Valor no valido.")
            if CModificar > repuesto.cantidad:
                print("El valor ingresado supera el Stock.")
            elif CModificar <= repuesto.cantidad:
                repuesto.cantidad = repuesto.cantidad - CModificar
                Estado3 = False
        
    def eliminarrepuresto(self):
        VEliminar = ""
        while VEliminar == "":
            try:
                VEliminar = input("\nIngresa el repuesto a eliminar: ")
            except ValueError:
                print("Valor no valido.")
        for repuesto in self.H:
            if repuesto == VEliminar:
                print(f"\nEl repuesto {VEliminar} ha sido eliminado.")
                self.H.pop()
            else:
                self.Temp.append(self)
                
        if not self.Temp:
            for elemento in self.Temp:
                self.H.append(elemento)