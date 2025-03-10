from collections import deque
import ObjVehiculos as ObjV

class Pila:
    def crearyllenarpilavehiculos(self):
        P = deque()
        self.P = P
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
                "\n--------------------------------",
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
