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
        self.cpcs = deque()
        self.ctablets = deque()
        self.cestudiantes = deque()

    def ingresoequipos(self):
        print("\n¿Qué desea registrar?:", "\n1. Pc.", "\n2. Tablet.")
        opcion = -1
        while opcion not in [1, 2]:
            try:
                opcion = int(input("Ingresa la opción: "))
            except ValueError:
                print("Valor no valido.")
        if opcion == 1:
            print("\nIngresa los datos del equipo: ")
            serial, marca, mram, dduro, precio, disponible = "", "", -1, -1, -1.0, ""
            while serial == "":
                serial = input("\nserial: ")
            while marca == "":
                marca = input("marca: ")
            while mram == -1:
                try:
                    mram = int(input("Capacidad memoria RAM: "))
                except ValueError:
                    print("Valor no valido.")
            while dduro == -1:
                try:
                    dduro = int(input("Disco duro: "))
                except ValueError:
                    print("Valor no valido.")
            while precio == -1.0:
                try:
                    precio = float(input("precio: "))
                except ValueError:
                    print("Valor no valido.")
            while disponible not in [1,2]:
                try:
                    disponible = int(input("disponible (1. Si/2. No): "))
                except ValueError:
                    print("Valor no valido.")
            if disponible == 1:
                disponible = "Disponible."
            elif disponible == 2:
                disponible = "No disponible."
            busquedapc,busquedapcnoexiste = True, True
            while busquedapc:
                if self.cpcs:
                    for i in self.cpcs:
                        if i.serial.lower() == serial.lower():
                            print(
                                "El dispositivo ya se encuentra registrado, se actualizan datos."
                            )
                            i.mram = mram
                            i.dduro = dduro
                            i.precio = precio
                            i.disponible = disponible
                            busquedapc = False
                            busquedapcnoexiste = False
                    if busquedapcnoexiste == True:
                        self.cpcs.append(ObjE.Pc(serial, marca, mram, dduro, precio, disponible.lower()))
                        print("\nRegistro exitoso.")
                        busquedapc = False
                else:
                    self.cpcs.append(ObjE.Pc(serial, marca, mram, dduro, precio, disponible.lower()))
                    print("\nRegistro exitoso.")
                    busquedapc = False
        elif opcion == 2:
            print("\nIngresa los datos del equipo: ")
            serial, marca, mram, tamano, precio, disponible = "","",-1,-1.0,-1.0,""
            while serial == "":
                serial = input("\nserial: ")
            while marca == "":
                marca = input("marca: ")
            while mram == -1:
                try:
                    mram = int(input("Capacidad memoria RAM: "))
                except ValueError:
                    print("Valor no valido.")
            while tamano == -1.0:
                try:
                    tamano = float(input("Tamaño: "))
                except ValueError:
                    print("Valor no valido.")
            while precio == -1.0:
                try:
                    precio = float(input("precio: "))
                except ValueError:
                    print("Valor no valido.")
            while disponible not in [1,2]:
                try:
                    disponible = int(input("disponible (1. Si/2. No): "))
                except ValueError:
                    print("Valor no valido.")
            if disponible == 1:
                disponible = "Disponible."
            elif disponible == 2:
                disponible = "No disponible."
            busquedatablet, busquedatabletnoexiste = True, True
            while busquedatablet:
                if self.ctablets:
                    for i in self.ctablets:
                        if i.serial.lower() == serial.lower():
                            print(
                                "El dispositivo ya se encuentra registrado, se actualizan datos."
                            )
                            i.mram = mram
                            i.tamano = tamano
                            i.precio = precio
                            i.disponible = disponible
                            busquedatablet = False
                            busquedatabletnoexiste = False
                    if busquedatabletnoexiste == True:
                        self.ctablets.append(ObjE.Tablet(serial, marca, mram, tamano, precio, disponible.lower()))
                        print("\nRegistro exitoso.")
                        busquedatablet = False
                else:
                    self.ctablets.append(ObjE.Tablet(serial, marca, mram, tamano, precio, disponible.lower()))
                    print("\nRegistro exitoso.")
                    busquedatablet = False

    def prestar(self):
        print("\nIngresa los datos del prestamo: ")
        tipoprestamo, serial, nomestudiante, carnet = -1, "", "", -1
        while nomestudiante == "":
            nomestudiante = input("\nNombre estudiante: ")
        while carnet == -1:
            try:
                carnet = int(input("No carnet: "))
            except ValueError:
                print("Valor no valido.")
        print("- Qué dispositivo desea prestar: \n1. Computador.\n2. Tablet.")
        while tipoprestamo not in [1,2]:
            try:
                tipoprestamo = int(input("\nIngresa una opción: "))
            except ValueError:
                print("Valor no valido.")   
        while serial == "":
            serial = input("\nserial: ")
            busquedaprestamo = True
            while busquedaprestamo:
                if tipoprestamo == 1:
                    if self.cpcs:
                        for i in self.cpcs:
                            if i.serial.lower() == serial.lower() and i.disponible.lower() == "disponible":
                                print("El dispositivo se encuentra registrado bajo las siguientes especificaciones:",
                                    f"\n- Serial: {i.serial}",
                                    f"\n- Marca: {i.marca}",
                                    f"\n- Ram: {i.mram}",
                                    f"\n- Disco duro: {i.dduro}",
                                    f"\n- Precio: {i.precio}",
                                    f"\n- Disponibilidad: {i.disponible}")
                                confirmarcompra = -1
                                while confirmarcompra not in [1,2]:
                                    try:
                                        confirmarcompra = int(input("Ingresa 1 para confirmar prestamo, o 0 para cancelar: "))
                                    except ValueError:
                                        print("Valor no valido.")
                                if confirmarcompra == 1:
                                    self.cestudiantes.append(ObjE.Estudiantes(serial,nomestudiante,carnet))
                                    i.disponible = "No disponible"
                                    busquedaprestamo = False
                                    print("Prestamo exitoso.")
                                    break
                                elif confirmarcompra == 0:
                                    print("Prestamo cancelado.")
                                    busquedaprestamo = False
                                    break
                            else:
                                print("\nEl dispositivo buscado no existe o no esta disponible, intenta nuevamente.")
                    else:
                        print("\nNo hay dispositivos disponible para prestamos.")
                        busquedaprestamo = False

                elif tipoprestamo == 2:
                    if self.ctablets:
                        for i in self.ctablets:
                            if i.serial.lower() == serial.lower() and i.disponible.lower() == "disponible":
                                print("El dispositivo se encuentra registrado bajo las siguientes especificaciones:",
                                    f"\n- Serial: {i.serial}",
                                    f"\n- Marca: {i.marca}",
                                    f"\n- Ram: {i.mram}",
                                    f"\n- Tamaño: {i.tamano}",
                                    f"\n- Precio: {i.precio}",
                                    f"\n- Disponibilidad: {i.disponible}")
                                confirmarcompra = -1
                                while confirmarcompra not in [1,2]:
                                    try:
                                        confirmarcompra = int(input("Ingresa 1 para confirmar prestamo, o 0 para cancelar: "))
                                    except ValueError:
                                        print("Valor no valido.")
                                if confirmarcompra == 1:
                                    self.cestudiantes.append(ObjE.Estudiantes(serial,nomestudiante,carnet))
                                    i.disponible = "No disponible"
                                    busquedaprestamo = False
                                    print("Prestamo exitoso.")
                                    break
                                elif confirmarcompra == 0:
                                    print("Prestamo cancelado.")
                                    busquedaprestamo = False
                                    break
                            else:
                                print("\nEl dispositivo buscado no existe o no esta disponible, intenta nuevamente.")
                    else:
                        print("\nNo hay dispositivos disponible para prestamos.")
                        busquedaprestamo = False

    def mostrarpc(self):
        if self.cpcs:
            print("\nLista de computadores:")
            count = 0
            for i in self.cpcs:
                count += 1
                print(
                    f"\nDispositivo {count}:",
                    f"\n- Serial: {i.serial}",
                    f"\n- Marca: {i.marca}",
                    f"\n- Ram: {i.mram}",
                    f"\n- Disco duro: {i.dduro}",
                    f"\n- Precio: {i.precio}",
                    f"\n- Disponibilidad: {i.disponible}"
                )
        else:
            print("\nNo hay computadores registrados")

    def mostrartablet(self):
        if self.ctablets:
            print("\nLista de tablet:")
            count = 0
            for i in self.ctablets:
                count += 1
                print(
                    f"\nDispositivo {count}:",
                    f"\n- Serial: {i.serial}",
                    f"\n- Marca: {i.marca}",
                    f"\n- Ram: {i.mram}",
                    f"\n- Tamaño: {i.tamano}",
                    f"\n- Precio: {i.precio}",
                    f"\n- Disponibilidad: {i.disponible}"
                )
        else:
            print("\nNo hay tablets registradas")

    def mostrarprestamos(self):
        if self.cestudiantes:
            print("\nLista de dispositivos en prestamo:")
            count = 0
            for i in self.cestudiantes:
                count += 1
                print(
                    f"\nDispositivo {count}:",
                    f"\n- Serial: {i.serial}",
                    f"\n- Estudiante: {i.nomestudiante}",
                    f"\n- Carnet: {i.carnet}"
                )
        else:
            print("\nNo hay prestamos registrados")
