from collections import deque
import ObjPrendas as ObjP

class Tienda:
    def __init__(self):
        self.inventarioP = deque()
        self.inventarioS = deque()
        self.inventarioT = deque()
        self.tempprenda = None
        
    def registro(self):
        estado = True
        while estado:
            M,R,P,C = "","",-1.0,-1
            print("\nIngresa las especificaciones de la prenda: ")
            while M == "":
                M = input("\nIngresa la marca: ")
            while R == "":
                R = input("Ingresa la referencia: ")
            while P < 0:
                try:
                    P = float(input("Ingresa el precio: "))
                except ValueError:
                    print("Valor no valido.")
            while C < 0:
                try:
                    C = int(input("Ingresa la cantidad: "))
                except ValueError:
                    print("Valor no valido.")
            if self.inventarioP:
                for prenda in self.inventarioP:
                    if prenda.marca == M:
#                        prenda.referencia = R
#                        prenda.precio = P
                        prenda.cantidad += C
                        print("\nEl producto a registrar ya existe, se actualiza información.")
                    else:
                        self.inventarioP.append(ObjP.Prendas(M,R,P,C))
                        print("\nRegistro exitoso.")
            elif not self.inventarioP:
                self.inventarioP.append(ObjP.Prendas(M,R,P,C))
                print("\nRegistro exitoso.")
            otro = ""
            while otro not in ["s","n"]:
                otro = input("\n¿Desea ingresar otro producto? (S/N): ")
                if otro.lower() == "n":
                    estado = False
                    break
    def busquedaproducto(self):
        if self.inventarioP:
            buscar = ""
            while buscar == "":
                buscar = input("\nIngresa el producto a buscar: ")
            for prenda in self.inventarioP:
                if prenda.marca == buscar:
                    self.tempprenda = prenda
                    print(f"\n- Marca: {prenda.marca}",
                          "\n- Referencia: {prenda.referencia}",
                          "\n- Precio: {prenda.precio}",
                          "\n- Cantidad: {prenda.cantidad}")
        else:
            print("\nInventario vacio.")
            
    def modificar(self):
        Objtienda = Tienda
        Objtienda.busquedaproducto()
        print("\n¿Qué dato desea modificar? \n1. Marca.\n2. Referencia.\n3. Precio.\n4. Cantidad.")
        opcion = 0
        while opcion not in [1,2,3,4]:
                try:
                    opcion = int(input("Ingresa la opción: "))
                except ValueError:
                    print("Valor no valido.")
        M,R,P,C = "","",-1.0,-1
        if opcion == 1:
            while M == "":
                M = input("\nIngresa la nueva marca: ")
            self.tempprenda.marca = M
            print("\nModificación exitosa.")
        elif opcion == 2:
            while R == "":
                R = input("Ingresa la nueva referencia: ")
            self.tempprenda.referencia = R
            print("\nModificación exitosa.")
        elif opcion == 3:
            while P < 0:
                try:
                    P = float(input("Ingresa el nueva precio: "))
                except ValueError:
                    print("Valor no valido.")
            self.tempprenda.precio = P
            print("\nModificación exitosa.")
        elif opcion == 4:
            while C < 0:
                try:
                    C = int(input("Ingresa la nueva cantidad: "))
                except ValueError:
                    print("Valor no valido.")
            self.tempprenda.cantidad = C
            print("\nModificación exitosa.")
            
    def venta(self):
        Objtienda = Tienda
        Objtienda.busquedaproducto()
        cantidad = -1
        while cantidad < 0:
            try:
                cantidad = int(input("Ingresa la cantidad a vender: "))
            except ValueError:
                print("Valor no valido.")
        if self.tempprenda.cantidad > cantidad:
            self.tempprenda.cantidad -= cantidad
            print(f"\nProducto vendido, nueva cantidad en stock {self.tempprenda.cantidad}")
        elif self.tempprenda.cantidad < cantidad:
            print("\nCantidad indicada excede el stock disponible.")
        elif cantidad < 0:
            print("Se indico un valor negativo, no es valido.")