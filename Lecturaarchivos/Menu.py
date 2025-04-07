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
