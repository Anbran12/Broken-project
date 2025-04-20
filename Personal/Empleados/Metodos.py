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
        
    def convertirlista(self):
        return [self.id,self.nombre,self.apellido,self.cedula,self.email,self.telefono,self.direccion,self.cargo,self.jefe,self.inactivo]
    
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
        cargos = ["Gerente General","Director de Finanzas (CFO)","Director de Operaciones (COO)","Gerente de Recursos Humanos","Jefe de Ventas","Coordinador de Marketing","Analista Financiero","Contador","Asistente Administrativo","Recepcionista","Desarrollador de Software","Diseñador Gráfico","Especialista en Atención al Cliente","Técnico de Soporte IT","Gerente de Proyecto","Ejecutivo de Ventas","Encargado de Logística","Auditor Interno","Community Manager","Oficinista o Auxiliar Administrativo"]
        self.entrycargo = ctk.CTkComboBox(ventanaregistro, values=cargos, state="readonly")
#        self.entrycargo = ctk.CTkEntry(ventanaregistro)
        self.entrycargo.grid(row=7, column=1, pady=7, padx=10)
        
        ctk.CTkLabel(ventanaregistro, text="Jefe").grid(row=8, column=0, pady=7, padx=10)
        self.entryjefe = ctk.CTkEntry(ventanaregistro)
        self.entryjefe.grid(row=8, column=1, pady=7, padx=10)        
        
        ctk.CTkButton(ventanaregistro, text="Registrar", command=self.validacionerror).grid(row=9, column=0, columnspan=2, pady=7, padx=10)
        
        
        
    def validacionerror(self):
        self.ventanaerror = ctk.CTkToplevel()
        self.ventanaerror.title("Error")
        self.ventanaerror.geometry("+750+350")
        self.ventanaerror.focus()
        self.ventanaerror.grab_set()
        
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
        
        ctk.CTkLabel(self.ventanaerror, text="Datos registados exitosamente.").pack(pady=15, padx=15)
        nombre = self.entrynombre.get()
        apellido = self.entryapellido.get()
        cedula = self.entrycedula.get()
        email = self.entryemail.get()
        telefono = self.entrytelefono.get()
        direccion = self.entrydireccion.get()
        cargo = self.entrycargo.get()
        jefe = self.entryjefe.get()
        
        with open("C:/Users/Anbran12/Documents/Python/Broken-project/Personal/Empleados/basededatos.csv", "a", newline="") as archivoregistro:
            registrarenarchivo = csv.writer(archivoregistro)
            nuevoregistro = Empleados(1,nombre,apellido,cedula,email,telefono,direccion,cargo,jefe)
            registrarenarchivo.writerow(nuevoregistro.convertirlista())
        
        ctk.CTkButton(self.ventanaerror, text="Aceptar", command=self.ventanaerror.destroy).pack(pady=5, padx=15)
        
    def mostrarregistros(self):
        self.ventanamostrarregistros = ctk.CTkToplevel()
        self.ventanamostrarregistros.grab_set()
        self.ventanamostrarregistros.focus()
        self.ventanamostrarregistros.title("Tabla de registros")
        self.ventanamostrarregistros.geometry("1000x600+300+100")
        
        