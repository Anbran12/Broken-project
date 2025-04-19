class FastFood:
    def __init__(self, nombre_cliente="", tipo="", cantidad=0, precio=0.0):
        self.nombre_cliente = nombre_cliente
        self.tipo = tipo
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return (f"NombreCliente: {self.nombre_cliente}\n"
                f"TipoComida: {self.tipo}\n"
                f"Cantidad: {self.cantidad}\n"
                f"Precio: {self.precio}\n"
                f"---------------------------------------")

class Method:
    def ingresar_pedido(self, pedidos, opt):
        opciones = {1: "Perro", 2: "Burger", 3: "Chorizo", 4: "French Fries"}
        if opt in opciones:
            tipo = opciones[opt]
        else:
            print("Opción inválida.")
            return pedidos

        nombre_cliente = input("Ingrese el Nombre del cliente: ")
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio: "))

        pedido = FastFood(nombre_cliente, tipo, cantidad, precio)
        pedidos.append(pedido)
        return pedidos

    def mostrar_turno(self, pedidos):
        if not pedidos:
            print("No hay Turnos disponibles.")
        else:
            for pedido in pedidos:
                print(pedido.nombre_cliente)

    def despachar(self, pedidos):
        if pedidos:
            pedidos.pop(0)
        else:
            print("No hay pedidos para despachar.")
        return pedidos
    
class Importar:
    def leer_archivo(self):
        pedidos = []
        try:
            with open("reyesPedidos.txt", "r", encoding="utf-8") as file:
                pedido_actual = None
                for line in file:
                    line = line.strip()
                    if line.startswith("NombreCliente: "):
                        if pedido_actual:
                            pedidos.append(pedido_actual)
                        pedido_actual = FastFood()
                        pedido_actual.nombre_cliente = line.split(": ")[1]
                    elif line.startswith("TipoComida: "):
                        pedido_actual.tipo = line.split(": ")[1]
                    elif line.startswith("Cantidad: "):
                        pedido_actual.cantidad = int(line.split(": ")[1])
                    elif line.startswith("Precio: "):
                        precio = line.split(": ")[1]
                        pedido_actual.precio = float(precio) if precio.lower() != "null" else 0.0
                if pedido_actual:
                    pedidos.append(pedido_actual)
            print("Archivo importado correctamente")
        except FileNotFoundError:
            print("El archivo no existe.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")
        return pedidos
    
class Exportar:
    def exportar_archivo(self, pedidos):
        with open("reyesPedidos.txt", "w", encoding="utf-8") as file:
            for pedido in pedidos:
                file.write(str(pedido) + "\n")
        print("Archivo exportado correctamente")

class Menu:
    def __init__(self):
        self.pedidos = []
        self.method = Method()
        self.exportar = Exportar()
        self.importar = Importar()

    def mostrar_menu(self):
        while True:
            print("\nBienvenidos a estructuras fries!!")
            print("1: Ingresar Pedido")
            print("2: Visualizar Turno")
            print("3: Despachar")
            print("4: Exportar Pedidos")
            print("5: Importar Pedidos")
            print("6: Salir")

            try:
                opt = int(input("Seleccione una opción: "))
            except ValueError:
                print("Opción no válida, intente de nuevo.")
                continue

            if opt == 1:
                print("\n1: Perro\n2: Burger\n3: Chorizo\n4: French Fries")
                try:
                    comida_opt = int(input("Seleccione el tipo de comida: "))
                    self.pedidos = self.method.ingresar_pedido(self.pedidos, comida_opt)
                except ValueError:
                    print("Entrada no válida.")
            elif opt == 2:
                self.method.mostrar_turno(self.pedidos)
            elif opt == 3:
                self.pedidos = self.method.despachar(self.pedidos)
            elif opt == 4:
                if self.pedidos:
                    self.exportar.exportar_archivo(self.pedidos)
                else:
                    print("No hay pedidos para exportar.")
            elif opt == 5:
                self.pedidos = self.importar.leer_archivo()
            elif opt == 6:
                print("Gracias por usar el sistema. Hasta pronto!")
                break
            else:
                print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu = Menu()
    menu.mostrar_menu()
