from collections import deque
import ObjVehiculos as ObjV

class Pila:
    def crearpilavehiculos(self):
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