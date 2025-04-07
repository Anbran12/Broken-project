class Exportar:
    def exportar_archivo(self, pedidos):
        with open("reyesPedidos.txt", "w", encoding="utf-8") as file:
            for pedido in pedidos:
                file.write(str(pedido) + "\n")
        print("Archivo exportado correctamente")
