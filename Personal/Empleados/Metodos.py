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
        self.entrycargo = ctk.CTkComboBox(self.ventanaregistro, values=self.cargos(), state="readonly")
        self.entrycargo.grid(row=7, column=1, pady=7, padx=10)
                
        ctk.CTkLabel(self.ventanaregistro, text="Jefe").grid(row=8, column=0, pady=7, padx=10)
        self.combojefe = ctk.CTkComboBox(self.ventanaregistro, values=self.jefes(), state="readonly")
        self.combojefe.grid(row=8, column=1, pady=7, padx=10)
        
        ctk.CTkButton(self.ventanaregistro, text="Cancelar", command=self.ventanaregistro.destroy).grid(row=9, column=0, pady=7, padx=10)
        ctk.CTkButton(self.ventanaregistro, text="Registrar", command=self.validacionerror).grid(row=9, column=1, pady=7, padx=10)
        
    def cargos(self):
        cargos = []
        with open("C:/Users/Anbran12/Documents/Python/Broken-project/Personal/Empleados/cargos.csv", "r", newline="", encoding='utf-8') as listacargos:
            lectorcargos = csv.reader(listacargos)
            for c in lectorcargos:
                cargos.append(c[0])
        return cargos        

    def jefes(self):
        listaextraccionjefes = []
        with open("C:/Users/Anbran12/Documents/Python/Broken-project/Personal/Empleados/basededatos.csv", "r", newline="", encoding='utf-8') as listajefes:
            lectorjefes = csv.reader(listajefes)
            next(lectorjefes)
            for c in lectorjefes:
                jefe = c[1]+" "+c[2]
                listaextraccionjefes.append(jefe)
        return listaextraccionjefes

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
        
        if not self.combojefe.get():
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
        direccion = '"'+self.entrydireccion.get()+'"'
        cargo = self.entrycargo.get()
        jefe = self.entryjefe.get()
        
        with open("C:/Users/Anbran12/Documents/Python/Broken-project/Personal/Empleados/basededatos.csv", "a", newline="", encoding='utf-8') as archivoregistro:
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
        
        with open("C:/Users/Anbran12/Documents/Python/Broken-project/Personal/Empleados/basededatos.csv", "r", newline="", encoding='utf-8') as mostrarregistros:
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
        
    def modificarregistros(self):
        self.ventanamodificar = ctk.CTkToplevel()
        self.ventanamodificar.title("Modificar datos.")
        self.ventanamodificar.grab_set()
        self.ventanamodificar.focus()
        self.ventanamodificar.geometry("+750+100")
        
        with open("C:/Users/Anbran12/Documents/Python/Broken-project/Personal/Empleados/basededatos.csv", "r", newline="", encoding='utf-8') as mostrarregistros:
            lector = csv.reader(mostrarregistros)
            
            self.listaderegistros = []
            for dato in lector:
                id,nombre,apellido,cedula,email,telefono,direccion,cargo,jefe,estado = dato
                self.listaderegistros.append(Empleados(id,nombre,apellido,cedula,email,telefono,direccion,cargo,jefe,estado))
        mostrarregistros.close()

        self.framemodificarbloquebusqueda = ctk.CTkFrame(self.ventanamodificar)
        self.framemodificarbloquebusqueda.grid(row=0,column=0, columnspan=3,pady=5,padx=5)
        
        self.datomodificarlabel = ctk.CTkLabel(self.framemodificarbloquebusqueda, text="Ingresa el id a buscar:")
        self.datomodificarlabel.grid(row=0,column=0,pady=5,padx=10)
        self.datomodificar = ctk.CTkEntry(self.framemodificarbloquebusqueda)
        self.datomodificar.grid(row=0,column=1,pady=5,padx=5)
        self.botonbusqueda = ctk.CTkButton(self.framemodificarbloquebusqueda, text="Buscar", command=self.buscardatos)
        self.botonbusqueda.grid(row=1,column=0,columnspan=2,pady=5,padx=5)
        
    def buscardatos(self):
        datonoencontrado = True
        for i in range(len(self.listaderegistros)):
            if self.listaderegistros[i].cedula == self.datomodificar.get():
                framemodificardatospersonales = ctk.CTkFrame(self.ventanamodificar)
                framemodificardatospersonales.grid(row=1,column=0, columnspan=3,pady=5,padx=5)
                framemodificardireccionesytelefonos = ctk.CTkFrame(self.ventanamodificar)
                framemodificardireccionesytelefonos.grid(row=2,column=0, columnspan=3,pady=5,padx=5)
                framemodificarcargo = ctk.CTkFrame(self.ventanamodificar)
                framemodificarcargo.grid(row=3,column=0, columnspan=3,pady=5,padx=5)
                framemodificarbotonera = ctk.CTkFrame(self.ventanamodificar)
                framemodificarbotonera.grid(row=4,column=0, columnspan=3,pady=5,padx=5)

                ctk.CTkLabel(framemodificardatospersonales,text="Datos personales: ").grid(row=0, column=0, columnspan=2, pady=5, padx=5)
                ctk.CTkLabel(framemodificardatospersonales,text="Cédula", width=100).grid(row=1, column=0, pady=5, padx=5)
                dato1 = ctk.CTkEntry(framemodificardatospersonales)
                dato1.insert(0,self.listaderegistros[i].cedula)
                dato1.grid(row=1, column=1, pady=5, padx=5)

                ctk.CTkLabel(framemodificardatospersonales,text="Nombre", width=100).grid(row=2, column=0, pady=5, padx=5)
                dato2 = ctk.CTkEntry(framemodificardatospersonales)
                dato2.insert(0,self.listaderegistros[i].nombre)
                dato2.grid(row=2, column=1, pady=5, padx=5)

                ctk.CTkLabel(framemodificardatospersonales,text="Apellido", width=100).grid(row=3, column=0, pady=5, padx=5)
                dato3 = ctk.CTkEntry(framemodificardatospersonales)
                dato3.insert(0,self.listaderegistros[i].apellido)
                dato3.grid(row=3, column=1, pady=5, padx=5)

                ctk.CTkLabel(framemodificardireccionesytelefonos, text="Direcciones y teléfonos: ").grid(row=0, column=0, columnspan=2, pady=5, padx=5)
                ctk.CTkLabel(framemodificardireccionesytelefonos, text="Email", width=100).grid(row=1, column=0, pady=5, padx=5)
                dato4 = ctk.CTkEntry(framemodificardireccionesytelefonos)
                dato4.insert(0,self.listaderegistros[i].email)
                dato4.grid(row=1, column=1, pady=5, padx=5)

                ctk.CTkLabel(framemodificardireccionesytelefonos, text="Teléfono", width=100).grid(row=2, column=0, pady=5, padx=5)
                dato5 = ctk.CTkEntry(framemodificardireccionesytelefonos)
                dato5.insert(0,self.listaderegistros[i].telefono)
                dato5.grid(row=2, column=1, pady=5, padx=5)

                ctk.CTkLabel(framemodificardireccionesytelefonos, text="Dirección", width=100).grid(row=3, column=0, pady=5, padx=5)
                dato6 = ctk.CTkEntry(framemodificardireccionesytelefonos)
                dato6.insert(0,self.listaderegistros[i].direccion)
                dato6.grid(row=3, column=1, pady=5, padx=5)

                ctk.CTkLabel(framemodificarcargo, text="Datos laborales: ").grid(row=0, column=0, columnspan=2, pady=5, padx=5)
                ctk.CTkLabel(framemodificarcargo, text="Cargo", width=100).grid(row=1, column=0, pady=5, padx=5)
                dato7 = ctk.CTkComboBox(framemodificarcargo, values=self.cargos(), state="readonly")
                dato7.set(self.listaderegistros[i].cargo)
                dato7.grid(row=1, column=1, pady=5, padx=5)

                ctk.CTkLabel(framemodificarcargo, text="Jefe", width=100).grid(row=2, column=0, pady=5, padx=5)
                dato8 = ctk.CTkComboBox(framemodificarcargo, values=self.jefes(), state="readonly")
                dato8.set(self.listaderegistros[i].jefe)
                dato8.grid(row=2, column=1, pady=5, padx=5)

                ctk.CTkLabel(framemodificarcargo, text="Estado", width=100).grid(row=3, column=0, pady=5, padx=5)
                dato9 = ctk.CTkComboBox(framemodificarcargo, values=["ACTIVO","INACTIVO"], state="readonly", )
                dato9.set(self.listaderegistros[i].inactivo)
                dato9.grid(row=3, column=1, pady=5, padx=5)

                ctk.CTkButton(framemodificarbotonera, text="Cancelar", width=100, command=self.ventanamodificar.destroy).grid(row=0, column=0, pady=5, padx=10)
                ctk.CTkButton(framemodificarbotonera, text="Registrar", width=100).grid(row=0, column=1, pady=5, padx=10)
                                
                datonoencontrado = False

        if datonoencontrado:
            topnoencontrado = ctk.CTkToplevel()
            topnoencontrado.title("")
            topnoencontrado.grab_set()
            topnoencontrado.focus()
            topnoencontrado.geometry("+800+350")
            ctk.CTkLabel(topnoencontrado,text="No se encontraron resultados.").pack(pady=15,padx=15)