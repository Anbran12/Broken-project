import customtkinter as ctk
from PIL import Image

basededatos = []

class Personas:
    def __init__(self, nombre, edad, sexo, animal):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.animal = animal
    def __str__(self):
        return f"\nNombre:{self.nombre}\nEdad:{self.edad}\nSexo:{self.sexo}\nAnimal:{self.animal}"

class Formulario:
    def __init__(self):
        self.menu = ctk.CTk()
        self.menu.geometry("+300+200")
        self.menu.resizable(False,False)

        imagen = ctk.CTkImage(light_image=Image.open("C:/Users/Anbran12/Documents/Python/Broken-project/Ventana/estadisticas.png"),
                            dark_image=Image.open("C:/Users/Anbran12/Documents/Python/Broken-project/Ventana/estadisticas.png"),
                            size=(200, 200))

        etiquetaimagen = ctk.CTkLabel(self.menu, image=imagen,text="")
        etiquetaimagen.grid(row=0, column= 0, pady=20, padx=20)

        marcobotones = ctk.CTkFrame(self.menu)
        marcobotones.grid(row= 0, column= 1, padx=20)

        botonregistro1 = ctk.CTkButton(marcobotones, width=100, height= 30, border_width=2, text="Registro", command=self.registro)
        botonregistro1.grid(row=0, column=0, pady=10, padx=20)

        botonregistro2 = ctk.CTkButton(marcobotones, width=100, height= 30, border_width=2, text="Prestamo")
        botonregistro2.grid(row=1, column=0, pady=10, padx=20)

        botonregistro3 = ctk.CTkButton(marcobotones, width=100, height= 30, border_width=2, text="Devolución")
        botonregistro3.grid(row=2, column=0, pady=10, padx=20)

        botonregistro4 = ctk.CTkButton(marcobotones, width=100, height= 30, border_width=2, command=self.mostrardatos, text="Mostrar datos")
        botonregistro4.grid(row=3, column=0, pady=10, padx=20)

        self.menu.mainloop()

    def volver_al_menu(self):
        self.pantallaregistro.destroy()
        self.menu.deiconify()

    def registro(self):
        self.menu.withdraw()
        self.pantallaregistro = ctk.CTkToplevel()
        self.pantallaregistro.title("Registro")
        self.pantallaregistro.geometry("+300+200")
        self.pantallaregistro.resizable(False,False)
        self.pantallaregistro.overrideredirect(True)

        frame = ctk.CTkFrame(self.pantallaregistro, width= 400, height= 150, border_color= "grey", border_width=2)
        frame.grid(row=0, pady= 25, padx=25)

        self.etiqueta1 = ctk.CTkLabel(frame, text="Nombre")
        self.etiqueta1.grid(row=0, column=0, pady=10, padx= 25)
        self.entrada1 = ctk.CTkEntry(frame)
        self.entrada1.grid(row=0, column=1, pady=10, padx= 10)

        self.etiqueta2 = ctk.CTkLabel(frame, text="Edad")
        self.etiqueta2.grid(row=1, column=0, pady=10, padx= 25)
        self.entrada2 = ctk.CTkEntry(frame)
        self.entrada2.grid(row=1, column=1, pady=10, padx= 10)

        self.etiqueta3 = ctk.CTkLabel(frame, text="Sexo")
        self.etiqueta3.grid(row=2, column=0, pady=10, padx= 25)
        self.combobox3 = ctk.CTkComboBox(frame,values=["Hombre","Mujer","Otro"],state="readonly")
        self.combobox3.set("Hombre")
        self.combobox3.grid(row=2, column=1, pady=10, padx= 10)

        self.etiqueta4 = ctk.CTkLabel(frame, text="¿Eres un mapache?")
        self.etiqueta4.grid(row=3, column=0, pady=10, padx= 25)
        self.checkbox4 = ctk.CTkCheckBox(frame, text="Mapache", border_width=2)
        self.checkbox4.grid(row=3, column=1, pady=10, padx= 10)
        ctk.CTkButton(frame, text="Registrar", command=self.ventanaerror).grid(row=4, column=1, pady=10, padx=10)
        ctk.CTkButton(self.pantallaregistro, text="Volver", command=self.volver_al_menu).grid(pady=10, padx=10)
        
        self.pantallaregistro.focus()
        self.pantallaregistro.grab_set()

    def mostrardatos(self):
        ventanamostrardatos = ctk.CTkToplevel()
        ventanamostrardatos.title("Datos")
        ventanamostrardatos.geometry("+300+200")
#        ventanamostrardatos.resizable(False,False)
        
        if basededatos:
            columnas = ["Nombre", "Edad", "Sexo", "Animal"]
            marcoencabezado = ctk.CTkFrame(ventanamostrardatos)
            marcodatos = ctk.CTkScrollableFrame(ventanamostrardatos,border_width=1,border_color="black")
            for i, nomcol in enumerate(columnas):
                ctk.CTkLabel(marcoencabezado, text=nomcol, pady=20, padx=10, width=200, wraplength=200).grid(row=0,column=i)
            for i in range(len(basededatos)):
                filas = [basededatos[i].nombre, basededatos[i].edad, basededatos[i].sexo, basededatos[i].animal]
                for j, textfila in enumerate(filas):
                    ctk.CTkLabel(marcodatos, text=textfila, pady=1, padx=2, width=200, wraplength=200).grid(row=i,column=j)
                print(basededatos[i].nombre,basededatos[i].edad,basededatos[i].sexo,basededatos[i].animal)
            marcoencabezado.pack(fill="x")
            marcodatos.pack(fill="x")
        else:
            ctk.CTkLabel(ventanamostrardatos, text="No hay datos por mostrar", pady=20, padx=50).pack()
        ventanamostrardatos.focus()
        ventanamostrardatos.grab_set()   
        
    def ventanaerror(self):
        error = ctk.CTkToplevel()
        error.geometry("+300+200")
        error.focus()
        error.grab_set()        
        error.resizable(False,False)
        
        if not self.entrada1.get():
            ctk.CTkLabel(error, text="El campo nombre debe estar diligenciado", pady=20, padx=20).pack()
            ctk.CTkButton(error, text="Aceptar", command=error.destroy).pack()
            return
        
        if not self.entrada2.get():
            ctk.CTkLabel(error, text="El campo edad debe estar diligenciado", pady=20, padx=20).pack()
            ctk.CTkButton(error, text="Aceptar", command=error.destroy).pack()
            return

        valor = self.entrada2.get()
        try:
            int(valor)
        except ValueError:
            ctk.CTkLabel(error, text="Valor ingresado en campo Edad no es valido, no es un número entero", pady=20, padx=20).pack()
            ctk.CTkButton(error, text="Aceptar", command=error.destroy).pack()
            return
            
        ctk.CTkLabel(error, text=f"Datos registrados exitosamente.", pady=20, padx=20).pack()
        nombre, edad, sexo, animal = self.entrada1.get(), self.entrada2.get(), self.combobox3.get(), self.checkbox4.get()
        basededatos.append(Personas(nombre, edad, sexo, animal))
        ctk.CTkButton(error, text="Aceptar", command=error.destroy).pack()

obj = Formulario()