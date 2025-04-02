from collections import deque
import tkinter as tk

class PcPrueba:
    def __init__(self, serial, marca, mram, dduro, precio, disponible):
        self.serial = serial
        self.marca = marca
        self.mram = mram
        self.dduro = dduro
        self.precio = precio
        self.disponible = disponible

class MetodosEquiposPrueba:
    def __init__(self):
        self.cpcs = deque()
        self.ctablets = deque()
        self.cestudiantes = deque()

    def asignarycerrarPrueba(self):
        serial = self.entryserial.get()
        marca = self.entrymarca.get()
        mram = self.entrymram.get()
        dduro = self.entrydduro.get()
        precio = self.entryprecio.get()

        # Verificación de disponibilidad
        if self.entrydisponible.get() == "1":
            disponible = "Disponible."
        elif self.entrydisponible.get() == "2":
            disponible = "No disponible."
        else:
            print("Valor de disponibilidad no válido.")
            return
        
        self.cpcs.append(PcPrueba(serial, marca, mram, dduro, precio, disponible))
        print("\nRegistro exitoso.")
        self.ventana.quit()

    def ingresoequiposPrueba(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ingresa los datos del equipo:")

        # Configuración de las etiquetas y campos de entrada
        etiquetaserial = tk.Label(self.ventana, text="Serial: ")
        etiquetaserial.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entryserial = tk.Entry(self.ventana)
        self.entryserial.grid(row=0, column=1, padx=10, pady=5)

        etiquetamarca = tk.Label(self.ventana, text="Marca: ")
        etiquetamarca.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entrymarca = tk.Entry(self.ventana)
        self.entrymarca.grid(row=1, column=1, padx=10, pady=5)

        etiquetamram = tk.Label(self.ventana, text="Ram: ")
        etiquetamram.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entrymram = tk.Entry(self.ventana)
        self.entrymram.grid(row=2, column=1, padx=10, pady=5)

        etiquetadduro = tk.Label(self.ventana, text="Disco duro: ")
        etiquetadduro.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entrydduro = tk.Entry(self.ventana)
        self.entrydduro.grid(row=3, column=1, padx=10, pady=5)

        etiquetaprecio = tk.Label(self.ventana, text="Precio: ")
        etiquetaprecio.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.entryprecio = tk.Entry(self.ventana)
        self.entryprecio.grid(row=4, column=1, padx=10, pady=5)

        etiquetadisponible = tk.Label(self.ventana, text="Disponibilidad (1. Disponible. / 2. No disponible.): ")
        etiquetadisponible.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.entrydisponible = tk.Entry(self.ventana)
        self.entrydisponible.grid(row=5, column=1, padx=10, pady=5)

        boton_asignar = tk.Button(self.ventana, text="Asignar y Cerrar", command=self.asignarycerrarPrueba)
        boton_asignar.grid(row=6, columnspan=2, pady=10)

        self.ventana.mainloop()

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


# Crear el objeto y ejecutar el ingreso de equipos
obj = MetodosEquiposPrueba()
obj.ingresoequiposPrueba()
obj.mostrarpc()