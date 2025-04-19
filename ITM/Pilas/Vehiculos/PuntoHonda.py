import Principal as P
class PuntoHonda:
    def puntohonda(self):
        Obj = P.VHonda()
        Obj.crearpila()
        estado5 = True
        while estado5:
            try:
                print("\nMenú: ",
                           "\n1. Ingresar registro.",
                           "\n2. Buscar registro.",
                           "\n3. Vender repuesto.",
                           "\n4. Eliminar registro.",
                           "\n5. Modificar registro.",
                           "\n0. Salir.")
                opcion = int(input("\nQue desea hacer: "))
                if opcion == 1:
                    Obj.ingresarrepuestos()
                elif opcion == 2:
                    Obj.buscarrepuesto()
                elif opcion == 3:
                    Obj.buscarrepuesto()
                    Obj.ventarepuesto()
                elif opcion == 4:
                    Obj.buscarrepuesto()
                    while True:
                        try:
                            decision = input("\nConfirme que desea eliminar el elemento buscado (S/N): ")
                            if decision.lower() == "s":
                                Obj.eliminarrepuresto()
                                break
                            else:
                                print("\nEl elemento no se ha eliminado.")
                                break
                        except ValueError:
                            print("\nOpción no valida.")
                elif opcion == 5:
                    Obj.buscarrepuesto()
                    Obj.modificarinformacion()
                elif opcion == 0:
                    print("Saliendo...")
                    break
            except ValueError:
                print("Opción no valida.")