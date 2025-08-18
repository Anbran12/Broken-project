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
label = ctk.CTkLabel(ventana, text= "Ingresa algo: ").pack() # Etiqueta de texto (Label)
frame = ctk.CTkFrame(ventana, width=200, height=100).pack() # Marco (Frame)
ingresousuario = ctk.CTkEntry(frame) # Cuandro de ingreso de datos (Entry)
ingresousuario.pack()
ingresousuario.get() # Captura de datos ingresados en el entry
boton = ctk.CTkButton(ventana, text="presionar", command="Aqui se asigna una función al boton.").pack() # Boton
ctk.CTkTabview(ventana) # Widget que permite tener pestañas (tabs), como en un navegador o configuraciones.
ventana.focus() # Hace foco en la ventana emergente (la ventana principal sigue siendo visible)
ventana.grab_set() # Desactiva la ventana principal mientras esta esté abierta (la ventana principal sigue siendo visible)
ventana.withdraw() # Ocultar ventana para ser reemplazada por otra de manera temporal.
ventana.deiconify() # Volver a mostrar ventana oculta con la instrucción anterior.
ventana.mainloop() # Obligatorio para que la ventana se muestre.
