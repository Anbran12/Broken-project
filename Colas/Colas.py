import ObjComidas as ObjC
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
