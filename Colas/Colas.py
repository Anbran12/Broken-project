import ObjComidas as ObjC
import ObjEquipos as ObjE
from collections import deque

class MetodosComidas:
    def __init__(self):
        self.colacomidas = deque()
        
    def ingresopedidos(self):
        print("\nMenú comidas:",
              "\n1. Hamburguesa.",
              "\n2. Perro caliente.",
              "\n3. Salchipapas.",
              "\n4. Burrito.")
        print("\nMenú bebidas:",
              "\n1. Gaseosa.",
              "\n2. Jugo.",
              "\n3. Soda.")
        
        print("\nIngresa los datos del pedido: ")
        U,T,B,P = "", -1, -1, -1.0
        while U == "":
            U = input("\nIngresa el nombre del cliente: ")
        while T not in [1,2,3,4]:
            try:            
                T = int(input("Ingresa la comida a comprar: "))
            except ValueError:
                print("Valor no valido.")
        while B not in [1,2,3]:
            try:
                B = int(input("Ingresa la bebida: "))
            except ValueError:
                print("Valor no valido.")
        while P < 0:
            try:
                P = float(input("Ingresa precio total: "))
            except ValueError:
                print("Valor no valido.")
class MetodosEquipos:
    def __init__(self):
        self.Cpcs = deque()
        self.Ctablets = deque()
        self.CEstudiantes = deque()
        
    def ingresoequipos(self):
        print("\n¿Qué desea registrar?:",
              "\n1. Pc.",
              "\n2. Tablet.")
        opcion = -1
        while opcion not in [1,2]:
            try:
                opcion = int(input("Ingresa la opción: "))
            except ValueError:
                print("Valor no valido.")
        if opcion == 1:
            print("\nIngresa los datos del equipo: ")
            Serial,Marca,MRam,Dduro,Precio,NomEstudiante,Carnet,Disponible = "", "", -1, -1, -1.0, "", -1, ""
            while Serial == "":
                Serial = input("\nSerial: ")
            while Marca == "":
                Marca = input("\nMarca: ")
            while MRam == -1:
                try:
                    MRam = int(input("Capacidad memoria RAM: "))
                except ValueError:
                    print("Valor no valido.")
            while Dduro == -1:
                try:
                    Dduro = int(input("Disco duro: "))
                except ValueError:
                    print("Valor no valido.")
            while Precio == -1.0:
                try:
                    Precio = float(input("Precio: "))
                except ValueError:
                    print("Valor no valido.")
            while Disponible == "":
                try:
                    Disponible = float(input("Disponible (Si/No): "))
                except ValueError:
                    print("Valor no valido.")
        elif opcion == 2:
            print("\nIngresa los datos del equipo: ")
            Serial,Tamano,Marca,MRam,Dduro,Precio,NomEstudiante,Carnet,Disponible = "", -1.0, "", -1, -1, -1.0, "", -1, ""
            while Serial == "":
                Serial = input("\nSerial: ")
            while Tamano == -1.0:
                try:
                    Tamano = float(input("Tamaño: "))
                except ValueError:
                    print("Valor no valido.")
            while Marca == "":
                Marca = input("\nMarca: ")
            while MRam == -1:
                try:
                    MRam = int(input("Capacidad memoria RAM: "))
                except ValueError:
                    print("Valor no valido.")
            while Dduro == -1:
                try:
                    Dduro = int(input("Disco duro: "))
                except ValueError:
                    print("Valor no valido.")
            while Precio == -1.0:
                try:
                    Precio = float(input("Precio: "))
                except ValueError:
                    print("Valor no valido.")
            while Disponible == "":
                try:
                    Disponible = float(input("Disponible (Si/No): "))
                except ValueError:
                    print("Valor no valido.")
    def prestar(self):
            print("\nIngresa los datos del prestamo: ")
            Serial,NomEstudiante,Carnet = "", "", -1
            while Serial == "":
                Serial = input("\nSerial: ")
            while Marca == "":
                Marca = input("\nNombre estudiante: ")
            while MRam == -1:
                try:
                    MRam = int(input("No carnet: "))
                except ValueError:
                    print("Valor no valido.")