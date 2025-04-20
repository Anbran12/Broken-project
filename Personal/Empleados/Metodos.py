import customtkinter as ctk
import csv

class Empleados:
    def __init__(self,id,nombre,apellido,cedula,email,telefono,direccion,cargo,jefe,inactivo="ACTIVO"):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.cargo = cargo
        self.jefe = jefe
        self.inactivo = inactivo

class MetodosEmpleados:
    def registroempledos(self):
        ventanaregistro = ctk.CTkToplevel()
        ventanaregistro.geometry("+750+100")
        ventanaregistro.focus()
        ventanaregistro.grab_set()
        ventanaregistro.title("Registro nueva persona")
#        nombre,apellido,cedula,email,telefono,direccion,cargo,jefe = -1, "", "", -1, "", -1, "", "", ""
        ctk.CTkLabel(ventanaregistro, text="Datos de la persona").grid(row=0, column=0, columnspan=2)
        
        ctk.CTkLabel(ventanaregistro, text="Nombre").grid(row=1, column=0, pady=7, padx=10)
        self.entrynombre = ctk.CTkEntry(ventanaregistro)
        self.entrynombre.grid(row=1, column=1, pady=7, padx=10)
        
        ctk.CTkLabel(ventanaregistro, text="Apellido").grid(row=2, column=0, pady=7, padx=10)
        self.entryapellido = ctk.CTkEntry(ventanaregistro)
        self.entryapellido.grid(row=2, column=1, pady=7, padx=10)
        
        ctk.CTkLabel(ventanaregistro, text="Cedula").grid(row=3, column=0, pady=7, padx=10)
        self.entrycedula = ctk.CTkEntry(ventanaregistro)
        self.entrycedula.grid(row=3, column=1, pady=7, padx=10)
        
        ctk.CTkLabel(ventanaregistro, text="Email").grid(row=4, column=0, pady=7, padx=10)
        self.entryemail = ctk.CTkEntry(ventanaregistro)
        self.entryemail.grid(row=4, column=1, pady=7, padx=10)
        
        ctk.CTkLabel(ventanaregistro, text="Telefono").grid(row=5, column=0, pady=7, padx=10)
        self.entrytelefono = ctk.CTkEntry(ventanaregistro)
        self.entrytelefono.grid(row=5, column=1, pady=7, padx=10)
        
        ctk.CTkLabel(ventanaregistro, text="Direccion").grid(row=6, column=0, pady=7, padx=10)
        self.entrydireccion = ctk.CTkEntry(ventanaregistro)
        self.entrydireccion.grid(row=6, column=1, pady=7, padx=10)
        
        ctk.CTkLabel(ventanaregistro, text="Cargo").grid(row=7, column=0, pady=7, padx=10)
        self.entrycargo = ctk.CTkEntry(ventanaregistro)
        self.entrycargo.grid(row=7, column=1, pady=7, padx=10)
        
        ctk.CTkLabel(ventanaregistro, text="Jefe").grid(row=8, column=0, pady=7, padx=10)
        self.entryjefe = ctk.CTkEntry(ventanaregistro)
        self.entryjefe.grid(row=8, column=1, pady=7, padx=10)        
        
        ctk.CTkButton(ventanaregistro, text="Pulsame", command=self.validacionerror).grid(row=9, column=0, columnspan=2)
        
        
        
    def validacionerror(self):
        ventanaerror = ctk.CTkToplevel()
        ventanaerror.title("Error")
        ventanaerror.geometry("+750+350")
        ventanaerror.focus()
        ventanaerror.grab_set()
        
        if not self.entrynombre.get():
            pass
        
        if not self.entryapellido.get():
            pass
        
        if not self.entrycedula.get():
            pass
        
        if not self.entryemail.get():
            pass
        
        if not self.entrytelefono.get():
            pass
        
        if not self.entrydireccion.get():
            pass
        
        if not self.entrycargo.get():
            pass
        
        if not self.entryjefe.get():
            pass        
