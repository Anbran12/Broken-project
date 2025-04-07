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
