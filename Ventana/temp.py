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
        menu = ctk.CTk()
        menu.geometry("+300+200")
        menu.resizable(False,False)

        imagen = ctk.CTkImage(light_image=Image.open("C:/Users/Anbran12/Documents/Python/Broken-project/Ventana/estadisticas.png"),
                            dark_image=Image.open("C:/Users/Anbran12/Documents/Python/Broken-project/Ventana/estadisticas.png"),
                            size=(200, 200))

        etiquetaimagen = ctk.CTkLabel(menu, image=imagen,text="")
        etiquetaimagen.grid(row=0, column= 0, pady=20, padx=20)

        marcobotones = ctk.CTkFrame(menu)
        marcobotones.grid(row= 0, column= 1, padx=20)

        botonregistro1 = ctk.CTkButton(marcobotones, width=100, height= 30, border_width=2, text="Registro", command=self.registro)
        botonregistro1.grid(row=0, column=0, pady=10, padx=20)

        botonregistro2 = ctk.CTkButton(marcobotones, width=100, height= 30, border_width=2, text="Prestamo")
        botonregistro2.grid(row=1, column=0, pady=10, padx=20)

        botonregistro3 = ctk.CTkButton(marcobotones, width=100, height= 30, border_width=2, text="Devolución")
        botonregistro3.grid(row=2, column=0, pady=10, padx=20)

        botonregistro4 = ctk.CTkButton(marcobotones, width=100, height= 30, border_width=2, command=self.mostrardatos, text="Mostrar datos")
        botonregistro4.grid(row=3, column=0, pady=10, padx=20)

        menu.mainloop()

    def registro(self):
        pantallaregistro = ctk.CTkToplevel()
        pantallaregistro.title("Registro")
        pantallaregistro.geometry("+300+200")
        pantallaregistro.resizable(False,False)

        frame = ctk.CTkFrame(pantallaregistro, width= 400, height= 150, border_color= "grey", border_width=2)
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
        boton4 = ctk.CTkButton(frame, text="Ventana 2", command=self.ventanaerror)
        boton4.grid(row=4, column=1, pady=10, padx=10)
        
        pantallaregistro.focus()
        pantallaregistro.grab_set()

    def mostrardatos(self):
        if basededatos:
            for i in range(len(basededatos)):
                print(basededatos[i])
        else:
            print("No hay datos para mostrar.")
    
    def ventana2(self):
        self.ventana2 = ctk.CTkToplevel()
        self.ventana2.title("Datos")
        self.ventana2.geometry("+300+200")
        self.ventana2.resizable(False,False)
        self.ventana2.focus()
        self.ventana2.grab_set()
        labelv2 = ctk.CTkLabel(self.ventana2, text="Datos ingresados:")
        labelv2.pack(pady=2,padx=10)
        framev2 = ctk.CTkFrame(self.ventana2, border_width=2, border_color="gray")
        framev2.pack(pady=10, padx=10)
        labelnombret = ctk.CTkLabel(framev2, text="Nombre:", width=100, height=30)
        labelnombret.grid(row=1,column=0, pady=5, padx=5)
        labelnombre = ctk.CTkLabel(framev2, text=self.entrada1.get(), width=100, height=30)
        labelnombre.grid(row=1,column=1, pady=5, padx=5)
        labelapellidot = ctk.CTkLabel(framev2, text="Apellido:", width=100, height=30)
        labelapellidot.grid(row=2,column=0)
        labelapellido = ctk.CTkLabel(framev2, text=self.entrada2.get(), width=100, height=30)
        labelapellido.grid(row=2,column=1)
        labelsexot = ctk.CTkLabel(framev2, text="Sexo:", width=100, height=30)
        labelsexot.grid(row=3,column=0, pady=5, padx=5)
        labelsexo = ctk.CTkLabel(framev2, text=self.combobox3.get(), width=100, height=30)
        labelsexo.grid(row=3,column=1, pady=5, padx=5)
        
        
        
    def ventanaerror(self):
        error = ctk.CTkToplevel()
        error.geometry("+300+200")
        error.focus()
        error.grab_set()        
        error.resizable(False,False)
        if not self.entrada1.get():
            ctk.CTkLabel(error, text="El campo nombre debe estar diligenciado", pady=20, padx=20).pack()
        else:
            if not self.entrada2.get():
                ctk.CTkLabel(error, text="El campo edad debe estar diligenciado", pady=20, padx=20).pack()
            else:
                if self.entrada2.get():
                    valor = self.entrada2.get()
                    try:
                        int(valor)
                    except ValueError:
                        ctk.CTkLabel(error, text="Valor ingresado en campo Edad no es valido, no es un número entero", pady=20, padx=20).pack()
                    ctk.CTkLabel(error, text=f"Datos registrados exitosamente.", pady=20, padx=20).pack()
                    nombre, edad, sexo, animal = self.entrada1.get(), self.entrada2.get(), self.combobox3.get(), self.checkbox4.get()
                    basededatos.append(Personas(nombre, edad, sexo, animal))
                    botoncerrar = ctk.CTkButton(error, text="Aceptar", command=error.destroy).pack()

obj = Formulario()