from collections import deque

class Pila:
    def crearyllenarpila(self):
        P = deque()
        self.P = P
        estado = True
        while estado:
            try:
                D = int(input("Ingresa un dato o cero para finalizar: "))
                if D != 0:
                    self.P.append(D)
                else:
                    estado = False
                    print("Ha salido.")
            except ValueError:
                print("Valor no valido")
            
        while len(P):
            print(self.P.pop())

    def eliminarregistro(self):
        estado = True
        while estado:
            try:
                D = int(input("Ingresa un dato a eliminar: "))
#                if D != 0:
#                    self.P.append(D)
#                else:
#                    estado = False
#                    print("Ha salido.")
#            except ValueError:
#                print("Valor no valido")

            
            
Objpila = Pila()
Objpila.crearyllenarpila()

    
        
class PilaLista:
    def crearyllenarpilaL(self):
        P = []
        estado = True
        while estado:
            try:
                D = int(input("Ingresa un dato o cero para finalizar: "))
                if D != 0:
                    P.append(D)
                else:
                    estado = False
                    print("Ha salido.")
            except ValueError:
                print("Valor no valido")
            
        while len(P):
            print(P.pop())

Objpila = PilaLista()
Objpila.crearyllenarpilaL()
