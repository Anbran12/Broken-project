import customtkinter as ctk

class Formulario:
    def __init__(self):
        tabladatos = ctk.CTk()
        tabladatos.geometry("+300+200")
        tabladatos.resizable(False,False)

        etiquetaencabezado1 = ctk.CTkLabel(tabladatos, text="Nombre")
        etiquetaencabezado1.grid(row=0, column= 0, pady=20, padx=20)
        etiquetaencabezado2 = ctk.CTkLabel(tabladatos, text="Edad")
        etiquetaencabezado2.grid(row=0, column= 1, pady=20, padx=20)
        etiquetaencabezado3 = ctk.CTkLabel(tabladatos, text="Sexo")
        etiquetaencabezado3.grid(row=0, column= 2, pady=20, padx=20)
        etiquetaencabezado4 = ctk.CTkLabel(tabladatos, text="Animal")
        etiquetaencabezado4.grid(row=0, column= 3, pady=20, padx=20)

#        marcobotones = ctk.CTkFrame(tabladatos)
#        marcobotones.grid(row= 0, column= 1, padx=20)
#
#        botonregistro1 = ctk.CTkButton(marcobotones, width=100, height= 30, border_width=2, text="Registro", command=self.registro)
#        botonregistro1.grid(row=0, column=0, pady=10, padx=20)
#
#        botonregistro2 = ctk.CTkButton(marcobotones, width=100, height= 30, border_width=2, text="Prestamo")
#        botonregistro2.grid(row=1, column=0, pady=10, padx=20)
#
#        botonregistro3 = ctk.CTkButton(marcobotones, width=100, height= 30, border_width=2, text="Devolución")
#        botonregistro3.grid(row=2, column=0, pady=10, padx=20)
#
#        botonregistro4 = ctk.CTkButton(marcobotones, width=100, height= 30, border_width=2, command=self.mostrardatos, text="Mostrar datos")
#        botonregistro4.grid(row=3, column=0, pady=10, padx=20)

        tabladatos.mainloop()

Obj = Formulario()

#---------------------------------------------------------------------------------------------------

import customtkinter as ctk

# Inicializa la ventana
ctk.set_appearance_mode("light")  # o "dark"
ctk.set_default_color_theme("blue")  # puedes cambiar el tema

app = ctk.CTk()
app.title("Tabla en CustomTkinter")
app.geometry("600x300")

# Datos de ejemplo para la tabla
columnas = ["ID", "Nombre", "Edad"]
datos = [
    [1, "Ana", 23],
    [2, "Luis", 30],
    [3, "Marta", 27]
]

# Frame para contener la tabla
tabla_frame = ctk.CTkFrame(app)
tabla_frame.pack(pady=20)

# Crear encabezados de columna
for j, col in enumerate(columnas):
    header = ctk.CTkLabel(tabla_frame, text=col, font=ctk.CTkFont(weight="bold"))
    header.grid(row=0, column=j, padx=10, pady=5)

# Crear las filas de la tabla
for i, fila in enumerate(datos):
    for j, valor in enumerate(fila):
        celda = ctk.CTkLabel(tabla_frame, text=str(valor))
        celda.grid(row=i+1, column=j, padx=10, pady=5)

app.mainloop()
