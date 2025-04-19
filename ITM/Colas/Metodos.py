import ObjComidas as ObjC
import ObjEquipos as ObjE
from collections import deque


class MetodosComidas:
    def __init__(self):
        self.colacomidas = deque()

    def ingresopedidos(self):
        print(
            "\nMenú comidas:",
            "\n1. Hamburguesa.",
            "\n2. Perro caliente.",
            "\n3. Salchipapas.",
            "\n4. Burrito.",
        )
        print("\nMenú bebidas:", "\n1. Gaseosa.", "\n2. Jugo.", "\n3. Soda.")

        print("\nIngresa los datos del pedido: ")
        U, T, B, P = "", -1, -1, -1.0
        while U == "":
            U = input("\nIngresa el nombre del cliente: ")
        while T not in [1, 2, 3, 4]:
            try:
                T = int(input("Ingresa la comida a comprar: "))
            except ValueError:
                print("Valor no valido.")
        while B not in [1, 2, 3]:
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
        ccomputador = deque()
        self.ccomputador = ccomputador
        ctablet = deque()
        self.ctablet = ctablet

    def registrocomputadores(self):
        varserial, varmarca, varmram, vardduro, varprecio, vardisponible = "", "", -1, -1, -1.0, True
        print("\nIngresa los datos del equipo: ")
        while varserial == "":
            varserial = input("\nIngresa el serial: ")
        while varmarca == "":
            varmarca = input("Ingresa la marca: ")
        while varmram < 0:
            try:
                varmram = int(input("Ingresa valor de la ram: "))
            except ValueError:
                print("Valor no valido")
        while vardduro < 0:
            try:
                vardduro = int(input("Ingresa valor del disco duro: "))
            except ValueError:
                print("Valor no valido")
        while varprecio < 0:
            try:
                varprecio = float(input("Ingresa precio: "))
            except ValueError:
                print("Valor no valido")
                
        estadobusqueda = True
        if self.ccomputador:
            for elemento in range(len(self.ccomputador)):
                validaciondeexistencia = self.ccomputador[elemento].serial.lower()
                if validaciondeexistencia == varserial.lower():
                    print(f"\nEl computador {varserial} ya existe, se actualiza registro con información indicada.")
                    self.ccomputador[elemento].mram = varmram
                    self.ccomputador[elemento].dduro = vardduro
                    self.ccomputador[elemento].precio = varprecio
                    estadobusqueda = False
            if estadobusqueda:
                self.ccomputador.append(ObjE.Computador(varserial, varmarca, varmram, vardduro, varprecio, "Sin asignar", vardisponible))
                print("\nRegistro exitoso.")
                estadobusqueda = True
        else: 
            self.ccomputador.append(ObjE.Computador(varserial, varmarca, varmram, vardduro, varprecio, "Sin asignar", vardisponible))
            print("\nRegistro exitoso.")
            estadobusqueda = True

    def registrotablets(self):
        varserial, varmarca, varmram, vartamano, varprecio, vardisponible = "", "", -1, -1.0, -1.0, True
        print("\nIngresa los datos del equipo: ")
        while varserial == "":
            varserial = input("\nIngresa el serial: ")
        while varmarca == "":
            varmarca = input("Ingresa la marca: ")
        while varmram < 0:
            try:
                varmram = int(input("Ingresa valor de la ram: "))
            except ValueError:
                print("Valor no valido")
        while vartamano < 0:
            try:
                vartamano = int(input("Ingresa valor del tamaño: "))
            except ValueError:
                print("Valor no valido")
        while varprecio < 0:
            try:
                varprecio = float(input("Ingresa precio: "))
            except ValueError:
                print("Valor no valido")
        
        estadobusqueda = True
        if self.ctablet:
            for elemento in range(len(self.ctablet)):
                validaciondeexistencia = self.ctablet[elemento].serial.lower()
                if validaciondeexistencia == varserial.lower():
                    print(f"\nLa tablet {varserial} ya existe, se actualiza registro con información indicada.")
                    self.ctablet[elemento].mram = varmram
                    self.ctablet[elemento].dduro = vartamano
                    self.ctablet[elemento].precio = varprecio
                    estadobusqueda = False
            if estadobusqueda:
                self.ctablet.append(ObjE.Tablet(varserial, varmarca, varmram, vartamano, varprecio, "Sin asignar", vardisponible))
                print("\nRegistro exitoso.")
                estadobusqueda = True
        else: 
            self.ctablet.append(ObjE.Tablet(varserial, varmarca, varmram, vartamano, varprecio, "Sin asignar", vardisponible))
            print("\nRegistro exitoso.")
            estadobusqueda = True

    def prestarcomputadores(self):
        varserial, varmarca, varmram, vartamano, varprecio, vardisponible = "", "", -1, -1.0, -1.0, True
        print("\nIngresa los datos del equipo a prestar: ")
        while varserial == "":
            varserial = input("\nIngresa el serial: ")
        
        estadobusqueda = True
        if self.ccomputador:
            for elemento in range(len(self.ccomputador)):
                validaciondeexistencia = self.ccomputador[elemento].serial.lower()
                validaciondedisponibilidad = self.ccomputador[elemento].disponible
                if validaciondeexistencia == varserial.lower() and validaciondedisponibilidad == True:
                    print(f"\nLa tablet {varserial} ya existe con los siguientes datos",
                        f"\nSerial: {self.ccomputador[elemento].serial}",
                        f"\nMarca: {self.ccomputador[elemento].marca}",
                        f"\nRam: {self.ccomputador[elemento].mram}",
                        f"\nD. Duro: {self.ccomputador[elemento].dduro}",
                        f"\nPrecio {self.ccomputador[elemento].precio}")
                    estadobusqueda = False
            if estadobusqueda:
                print("\nEl dispositivo buscado no existe o no esta disponible.")
                estadobusqueda = True
        else: 
            print("\nNo hay dispositivos disponibles para pestamo.")
            estadobusqueda = True
        

########################################################################################################################################

    def mostrarcomputadores(self):
        if self.ccomputador:
            contador = 0
            for elemento in range(len(self.ccomputador)):
                contador += 1
                print(f"\nComputador {contador}:",
                      f"\nSerial: {self.ccomputador[elemento].serial}",
                      f"\nMarca: {self.ccomputador[elemento].marca}",
                      f"\nRam: {self.ccomputador[elemento].mram}",
                      f"\nD. Duro: {self.ccomputador[elemento].dduro}",
                      f"\nPrecio {self.ccomputador[elemento].precio}",
                      f"\nDisponible: {self.ccomputador[elemento].disponible}",
                      f"\nUsuario asignado: {self.ccomputador[elemento].usuario}")
        else: 
            print("\nNo hay computadores registrados.")

    def mostrartablets(self):
        if self.ctablet:
            contador = 0
            for elemento in range(len(self.ctablet)):
                contador += 1
                print(f"\nTablet {contador}:",
                      f"\nSerial: {self.ctablet[elemento].serial}",
                      f"\nMarca: {self.ctablet[elemento].marca}",
                      f"\nRam: {self.ctablet[elemento].mram}",
                      f"\nD. Duro: {self.ctablet[elemento].tamano}",
                      f"\nPrecio {self.ctablet[elemento].precio}",
                      f"\nDisponible: {self.ctablet[elemento].disponible}",
                      f"\nUsuario asignado: {self.ctablet[elemento].usuario}")
        else: 
            print("\nNo tablets registradas.")
        
        #ObjE.Computador(varserial, varmarca, varmram, vardduro, varprecio, usuario="Sin asignar", vardisponible)