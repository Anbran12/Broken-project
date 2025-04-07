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