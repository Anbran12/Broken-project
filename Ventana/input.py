# https://www.youtube.com/playlist?list=PL7HAy5R0ehQXb2aFKOKyeCMequxyb5jzJ

import tkinter as tk

def ingresouser():
    ingresousuario1 = ingresousuario.get()
    label2.config(text=f"{ingresousuario1}")

ventana = tk.Tk()

ventana.title("Ventanita.") # Indicarle título a la ventana.
ventana.geometry("500x500+200+30") # Indicar tamaño de ventana "500x500 corresponte al tamaño y +200+30" corresponde a la ubicación.
ventana.minsize(500,300) # Tamaño mínimo de la ventana.
ventana.maxsize(1000, 600) # Tamaño máximo de la ventana.
#ventana.iconbitmap("User.ico") # Indicar un icono a la parte superior izquierda a la ventana.
ventana.configure(bg="grey") # Indicar color de fondo de la ventana.
ventana.resizable(False,False) # Bloquear el tamaño de la ventana.
ventana.attributes("-alpha",1) # Con -alpha y un valor se puede definir la transparencia de la ventana.

label1 = tk.Label(ventana, text= "Ingresa algo: ")
label1.pack()
frame1 = tk.Frame(ventana, width=200, height=100, bg="lightblue")
frame1.pack()
ingresousuario = tk.Entry(frame1)
ingresousuario.pack()

boton = tk.Button(ventana, text="presionar", command=ingresouser)
boton.pack()

label2 = tk.Label(ventana, text="Texto 1")
label2.pack()

ventana.mainloop()