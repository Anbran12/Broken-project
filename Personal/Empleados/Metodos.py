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
        self.ventanaregistro = ctk.CTkToplevel()
        self.ventanaregistro.geometry("+750+100")
        self.ventanaregistro.focus()
        self.ventanaregistro.grab_set()
        self.ventanaregistro.title("Registro nueva persona")
        self.ventanaregistro.resizable(False,False)
#        nombre,apellido,cedula,email,telefono,direccion,cargo,jefe = -1, "", "", -1, "", -1, "", "", ""
        ctk.CTkLabel(self.ventanaregistro, text="Datos de la persona").grid(row=0, column=0, columnspan=2)
        
        ctk.CTkLabel(self.ventanaregistro, text="Nombre", width=150).grid(row=1, column=0, pady=7, padx=10)
        self.entrynombre = ctk.CTkEntry(self.ventanaregistro)
        self.entrynombre.grid(row=1, column=1, pady=7, padx=10)
        
        ctk.CTkLabel(self.ventanaregistro, text="Apellido").grid(row=2, column=0, pady=7, padx=10)
        self.entryapellido = ctk.CTkEntry(self.ventanaregistro)
        self.entryapellido.grid(row=2, column=1, pady=7, padx=10)
        
        ctk.CTkLabel(self.ventanaregistro, text="Cedula").grid(row=3, column=0, pady=7, padx=10)
        self.entrycedula = ctk.CTkEntry(self.ventanaregistro)
        self.entrycedula.grid(row=3, column=1, pady=7, padx=10)
        
        ctk.CTkLabel(self.ventanaregistro, text="Email").grid(row=4, column=0, pady=7, padx=10)
        self.entryemail = ctk.CTkEntry(self.ventanaregistro)
        self.entryemail.grid(row=4, column=1, pady=7, padx=10)
        
        ctk.CTkLabel(self.ventanaregistro, text="Telefono").grid(row=5, column=0, pady=7, padx=10)
        self.entrytelefono = ctk.CTkEntry(self.ventanaregistro)
        self.entrytelefono.grid(row=5, column=1, pady=7, padx=10)
        
        ctk.CTkLabel(self.ventanaregistro, text="Direccion").grid(row=6, column=0, pady=7, padx=10)
        self.entrydireccion = ctk.CTkEntry(self.ventanaregistro)
        self.entrydireccion.grid(row=6, column=1, pady=7, padx=10)
        
        ctk.CTkLabel(self.ventanaregistro, text="Cargo").grid(row=7, column=0, pady=7, padx=10)
        cargos = ["Gerente General","Director de Finanzas (CFO)","Director de Operaciones (COO)","Gerente de Recursos Humanos","Jefe de Ventas","Coordinador de Marketing","Analista Financiero","Contador","Asistente Administrativo","Recepcionista","Desarrollador de Software","Diseñador Gráfico","Especialista en Atención al Cliente","Técnico de Soporte IT","Gerente de Proyecto","Ejecutivo de Ventas","Encargado de Logística","Auditor Interno","Community Manager","Oficinista o Auxiliar Administrativo"]
        self.entrycargo = ctk.CTkComboBox(self.ventanaregistro, values=cargos, state="readonly")
#        self.entrycargo = ctk.CTkEntry(self.ventanaregistro)
        self.entrycargo.grid(row=7, column=1, pady=7, padx=10)
        
        ctk.CTkLabel(self.ventanaregistro, text="Jefe").grid(row=8, column=0, pady=7, padx=10)
        self.entryjefe = ctk.CTkEntry(self.ventanaregistro)
        self.entryjefe.grid(row=8, column=1, pady=7, padx=10)
        
        ctk.CTkButton(self.ventanaregistro, text="Cancelar", command=self.ventanaregistro.destroy).grid(row=9, column=0, pady=7, padx=10)
        ctk.CTkButton(self.ventanaregistro, text="Registrar", command=self.validacionerror).grid(row=9, column=1, pady=7, padx=10)
        
        
        
    def validacionerror(self):
        self.ventanaerror = ctk.CTkToplevel()
        self.ventanaerror.title("Mensaje:")
        self.ventanaerror.geometry("+750+350")
        self.ventanaerror.focus()
        self.ventanaerror.grab_set()
        self.ventanaerror.resizable(False,False)
        
        listaerrores = []
        
        if not self.entrynombre.get():
            listaerrores.append("Ingresar nombre")
        
        if not self.entryapellido.get():
            listaerrores.append("Ingresar apellido")
        
        if not self.entrycedula.get():
            listaerrores.append("Ingresar cédula")
        elif self.entrycedula.get():
            try:
                int(self.entrycedula.get())
            except BaseException:
                listaerrores.append("Cédula: Valor ingresado no valido")
        
        if not self.entryemail.get():
            listaerrores.append("Ingresar email")
        
        if not self.entrytelefono.get():
            listaerrores.append("Ingresar telefono")
        elif self.entrytelefono.get():
            try:
                int(self.entrytelefono.get())
            except BaseException:
                listaerrores.append("Teléfono: Valor ingresado no valido")
        
        if not self.entrydireccion.get():
            listaerrores.append("Ingresar dirección")
        
        if not self.entrycargo.get():
            listaerrores.append("Ingresar cargo")
        
        if not self.entryjefe.get():
            listaerrores.append("Ingresar jefe")
            
        if listaerrores:
            ctk.CTkLabel(self.ventanaerror, text="Los siguientes campos contienen errores o están vacíos:").pack(pady=10, padx=10)
            framelistaerrores = ctk.CTkScrollableFrame(self.ventanaerror, width=350, height=150)
            framelistaerrores.pack(pady=5, padx=3)
            for i, j in enumerate(listaerrores):
                ctk.CTkLabel(framelistaerrores, text=f"{i+1}. {j}", wraplength=335, justify="left", anchor="w").pack(padx=2, anchor="w")
            return
        
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
            archivoregistro.close()
        
        ctk.CTkButton(self.ventanaerror, text="Aceptar", command=self.ventanaerror.destroy).pack(pady=5, padx=15)
        
    def mostrarregistros(self):
        self.ventanamostrarregistros = ctk.CTkToplevel()
        self.ventanamostrarregistros.grab_set()
        self.ventanamostrarregistros.focus()
        self.ventanamostrarregistros.title("Tabla de registros")
        self.ventanamostrarregistros.geometry("1030x600+300+100")
        cabecera = ctk.CTkFrame(self.ventanamostrarregistros)
        cabecera.pack(pady=5, padx=5)
        datos = ctk.CTkScrollableFrame(self.ventanamostrarregistros, width=1000, height=550)
        datos.pack(pady=5, padx=5)
        
        with open("C:/Users/Anbran12/Documents/Python/Broken-project/Personal/Empleados/basededatos.csv", "r", newline="") as mostrarregistros:
            lectordatos = csv.reader(mostrarregistros)
            cabeceradatos = ["Id","Nombre","Apellido","Cédula","Email","Teléfono","Dirección","Cargo","Jefe", "Estado"]
            for columna, dato in enumerate(cabeceradatos):
                ctk.CTkLabel(cabecera,text=dato,width=100, wraplength=100).grid(row=0, column=columna)
            next(lectordatos)
            for j, registro in enumerate(lectordatos):
                id,nombre,apellido,cedula,email,telefono,direccion,cargo,jefe,estado = registro
                listadatos = [id,nombre,apellido,cedula,email,telefono,direccion,cargo,jefe,estado]
                for i, dato in enumerate(listadatos):
                    ctk.CTkLabel(datos, text=dato, width=100, wraplength=100).grid(row=j, column=i)

            mostrarregistros.close()
        
        