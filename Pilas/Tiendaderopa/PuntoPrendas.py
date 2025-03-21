import Principal as P
class Prendas:
    def prenda(self):
        while True:
            print("\n¿Que desea hacer?",
                "\n1. Registrar productos.",
                "\n2. Constultar productos.",
                "\n3. Modificar productos.",
                "\n4. Vender productos.",
                "\n0. Salir.")
            Obj = P.Tienda()
            opcion = -1
            while opcion not in [0,1,2,3,4]:
                    try:
                        opcion = int(input("Ingresa la opción: "))
                    except ValueError:
                        print("Valor no valido.")
            if opcion == 1:
                Obj.registro()
            elif opcion == 2:
                Obj.busquedaproducto()
            elif opcion == 3:
                Obj.busquedaproducto()
                Obj.modificar()
            elif opcion == 4:
                Obj.busquedaproducto()
                Obj.venta()
            elif opcion == 0:
                print("Saliendo...")
                break