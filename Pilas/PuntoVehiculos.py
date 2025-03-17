import Principal as P

class PuntoVehiculos:
    def puntovehiculos(self):
        Objpila = P.Pila()
        Objpila.crearpilageneral()
        Objpila.llenarpilavehiculos()
        estado5 = True
        while estado5:
            try:
                print("\nQue desea hacer: ",
                           "\n1. Ingresar más registros.",
                           "\n2. Mostrar todos los registros.",
                           "\n3. Eliminar registro.",
                           "\n4. Modificar registro.",
                           "\n0. Salir.")
                opcion = int(input())
                if opcion == 1:
                    Objpila.llenarpilavehiculos()
                elif opcion == 2:
                    Objpila.mostrarregistrosvehiculos()
                elif opcion == 3:
                    Objpila.eliminarregistrovehiculos()
                elif opcion == 4:
                    Objpila.modificarobjeto()
                elif opcion == 0:
                    print("Saliendo...")
                    break
            except ValueError:
                print("Opción no valida.")