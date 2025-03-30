# https://www.youtube.com/playlist?list=PL7HAy5R0ehQXb2aFKOKyeCMequxyb5jzJ

import tkinter as tk

ventana = tk.Tk()

ventana.title("Ventanita.") # Indicarle título a la ventana.
ventana.geometry("500x500+200+30") # Indicar tamaño de ventana "500x500 corresponte al tamaño y +200+30" corresponde a la ubicación.
ventana.minsize(500,300) # Tamaño mínimo de la ventana.
ventana.maxsize(1000, 600) # Tamaño máximo de la ventana.
ventana.iconbitmap("User.ico") # Indicar un icono a la parte superior izquierda a la ventana.
ventana.configure(bg="grey") # Indicar color de fondo de la ventana.
ventana.resizable(False,False) # Bloquear el tamaño de la ventana.
ventana.attributes("-alpha",0.9) # Con -alpha y un valor se puede definir la transparencia de la ventana.

ventana.mainloop()