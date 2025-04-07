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
