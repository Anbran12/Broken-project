import Principal as P

class PuntoVehiculos:
    def puntovehiculos(self):
        Objpila = P.Pila()
        Objpila.crearpilavehiculos()
        Objpila.llenarpilavehiculos()
        estado5 = True
        while estado5:
            try:
                opcion = int(input("Que desea hacer: ",
                           "1. Ingresar más registros.",
                           "2. Mostrar todos los registros.",
                           "3. Eliminar registro.",
                           "4. Modificar registro."))
                if opcion == 1:
                    Objpila.llenarpilavehiculos()
                elif opcion == 2:
                    Objpila.mostrarregistrosvehiculos()
                elif opcion == 3:
                    Objpila.eliminarregistrovehiculos()
                elif opcion == 4:
                    Objpila.modificarobjeto()
            except ValueError:
                print("Opción no valida.")