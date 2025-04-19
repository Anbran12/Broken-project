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

#-------------------------------------------------------------------------------------------------

import customtkinter as ctk

# Simulando datos (puedes usar tus objetos reales aquí)
class Animalito:
    def __init__(self, nombre, edad, sexo, animal):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.animal = animal

basededatos = [
    Animalito("Luna", 3, "Hembra", "Perro"),
    Animalito("Max", 5, "Macho", "Gato"),
    Animalito("Coco", 2, "Macho", "Loro"),
    Animalito("Nina", 4, "Hembra", "Conejo"),
]

# Crear ventana principal
ventanamostrardatos = ctk.CTk()
ventanamostrardatos.geometry("600x400")
ventanamostrardatos.title("Tabla de Datos")

# Contenedor principal para la tabla
contenedor_tabla = ctk.CTkFrame(ventanamostrardatos)
contenedor_tabla.pack(padx=10, pady=10, fill="both", expand=True)

# Encabezados de columna
columnas = ["Nombre", "Edad", "Sexo", "Animal"]
marcoencabezado = ctk.CTkFrame(contenedor_tabla)
marcoencabezado.pack(fill="x")

for i, nomcol in enumerate(columnas):
    label = ctk.CTkLabel(
        marcoencabezado,
        text=nomcol,
        font=ctk.CTkFont(size=14, weight="bold"),
        padx=10, pady=10,
        width=120,
        anchor="w"  # alinea a la izquierda
    )
    label.grid(row=0, column=i)

# Datos con scroll
marcodatos = ctk.CTkScrollableFrame(contenedor_tabla, border_width=1, border_color="gray")
marcodatos.pack(fill="both", expand=True)

# Mostrar datos
for i, dato in enumerate(basededatos):
    valores = [dato.nombre, dato.edad, dato.sexo, dato.animal]
    for j, valor in enumerate(valores):
        color_fondo = "#f0f0f0" if i % 2 == 0 else "#e0e0e0"  # estilo tipo rayado
        label = ctk.CTkLabel(
            marcodatos,
            text=valor,
            padx=10, pady=5,
            width=120,
            anchor="w",
            fg_color=color_fondo
        )
        label.grid(row=i, column=j)

# Ejecutar la interfaz
ventanamostrardatos.mainloop()


#-----------------------------------------------------------------------------------------------------

import customtkinter as ctk

# Inicializar
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("400x300")
root.overrideredirect(True)  # Sin barra de título ni borde de SO

# Simular un borde con un frame externo
border_thickness = 4

border = ctk.CTkFrame(root, corner_radius=0, fg_color="#00aaff")
border.pack(padx=0, pady=0, fill="both", expand=True)

# Frame interior que representa el "contenido"
content = ctk.CTkFrame(border, corner_radius=10)
content.pack(padx=border_thickness, pady=border_thickness, fill="both", expand=True)

# Botón de cierre
close_button = ctk.CTkButton(content, text="Cerrar", command=root.destroy)
close_button.pack(pady=20)

root.mainloop()
