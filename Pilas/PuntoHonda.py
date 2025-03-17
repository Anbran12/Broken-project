import Principal as P
class PuntoHonda:
    def puntohonda(self):
        Obj = P.VHonda()
        estado5 = True
        while estado5:
            try:
                print("\nQue desea hacer: ",
                           "\n1. Ingresar registro.",
                           "\n2. Buscar registro.",
                           "\n3. Vender repuesto.",
                           "\n4. Eliminar registro.",
                           "\n5. Modificar registro.",
                           "\n0. Salir.")
                opcion = int(input())
                if opcion == 1:
                    Obj.ingresarrepuestos()
                elif opcion == 2:
                    Obj.buscarrepuesto()
                elif opcion == 3:
                    Obj.ventarepuesto()
                elif opcion == 4:
                    Obj.eliminarrepuresto()
                elif opcion == 5:
                    Obj.modificarinformacion()
                elif opcion == 0:
                    print("Saliendo...")
                    break
            except ValueError:
                print("Opción no valida.")