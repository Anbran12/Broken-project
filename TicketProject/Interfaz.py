from customtkinter import CTk, CTkButton, CTkToplevel, CTkTabview, CTkCheckBox, CTkComboBox, CTkEntry, CTkLabel, CTkFrame, CTkOptionMenu, CTkScrollableFrame

class Pagina_Principal:
    def __init__(self):
        ventana_principal = CTk()
        ventana_principal.geometry("1000x600+300+100")
        ventana_principal.title("QuickFlow")
        ventana_principal.resizable(False,False)

        barra_opciones = CTkFrame(ventana_principal, 980, 60, fg_color="#3A3A3A", corner_radius=15)
        barra_opciones.pack(pady=5, padx=5, fill="x", expand=False)

        espacio_general = CTkFrame(ventana_principal)
        espacio_general.pack(pady=5, padx=5, fill="both", expand=True)

        CTkEntry(barra_opciones, placeholder_text="Criterio de busqueda", border_width=2, font=(None, 16), width=230, height=32).grid(pady=10, padx=10, row=0, column=2)
        CTkButton(barra_opciones, text="Opción 1", border_width=2, corner_radius=15, font=(None, 16), width=32, height=32).grid(pady=10, padx=10, row=0, column=3)
        CTkButton(barra_opciones, text="Opción 2", border_width=2, corner_radius=15, font=(None, 16), width=32, height=32).grid(pady=10, padx=10, row=0, column=4)
        CTkButton(barra_opciones, text="Opción 3", border_width=2, corner_radius=15, font=(None, 16), width=32, height=32).grid(pady=10, padx=10, row=0, column=5)

        ventana_principal.mainloop()