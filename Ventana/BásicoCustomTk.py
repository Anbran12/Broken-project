import customtkinter as ctk

ventana = ctk.CTk() # Crear la ventana principal
ventana.title("Ventanita.") # Indicarle título a la ventana.
ventana.geometry("500x500+200+30") # Indicar tamaño de ventana "500x500 corresponte al tamaño y +200+30" corresponde a la ubicación.
ventana.minsize(500,300) # Tamaño mínimo de la ventana.
ventana.maxsize(1000, 600) # Tamaño máximo de la ventana.
#ventana.iconbitmap("User.ico") # Indicar un icono a la parte superior izquierda a la ventana.
ventana.configure(bg="grey") # Indicar color de fondo de la ventana.
ventana.resizable(False,False) # Bloquear el tamaño de la ventana.
ventana.attributes("-alpha",1) # Con -alpha y un valor se puede definir la transparencia de la ventana.

# Etiqueta de texto (Label)
label = ctk.CTkLabel(ventana, text= "Ingresa algo: ")
label.pack()
# Marco (Frame)
frame = ctk.CTkFrame(ventana, width=200, height=100)
frame.pack()
# Cuandro de ingreso de datos (Entry)
ingresousuario = ctk.CTkEntry(frame)
ingresousuario.pack()
# Boton
boton = ctk.CTkButton(ventana, text="presionar", command="Aqui se asigna una función al boton.")
boton.pack()

# Obligatorio para que la ventana se muestre.
ventana.mainloop()