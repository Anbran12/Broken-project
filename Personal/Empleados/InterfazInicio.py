import customtkinter as ctk
import Metodos as Mt

class Interfaz:
    def __init__(self):
        self.ventanainicio = ctk.CTk()
        self.ventanainicio.geometry("1000x600+300+100")
        self.ventanainicio.title("General")
        self.ventanainicio.resizable(False,False)
        
        ctk.CTkLabel(self.ventanainicio, text="Panel de opciones").pack(pady=10)
        ctk.CTkButton(self.ventanainicio, text="Registro", command=self.registro).pack(pady=10)
        ctk.CTkButton(self.ventanainicio, text="Modificar").pack(pady=10)
        ctk.CTkButton(self.ventanainicio, text="Buscar por id").pack(pady=10)
        ctk.CTkButton(self.ventanainicio, text="Buscar por jefe").pack(pady=10)
        ctk.CTkButton(self.ventanainicio, text="Mostrar registros").pack(pady=10)
        ctk.CTkButton(self.ventanainicio, text="Salir", hover_color="black", command=self.ventanainicio.destroy).pack(pady=10)
        
        self.ventanainicio.mainloop()

    def registro(self):
        a = Mt.MetodosEmpleados()
        a.registroempledos()


prueba = Interfaz()