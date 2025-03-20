import Principal as P
class Prendas:
    def prenda(self):
        print("¿Que desea hacer?",
              "\n1. Registrar productos.",
              "\n2. Constultar productos.",
              "\n3. Modificar productos.",
              "\n4. Vender productos.")
        Obj = P.Tienda()
        opcion = 0
        while opcion not in [1,2,3,4]:
                try:
                    opcion = int(input("Ingresa la opción: "))
                except ValueError:
                    print("Valor no valido.")
        if opcion == 1:
            Obj.registro()
        elif opcion == 2:
            Obj.busquedaproducto()
        elif opcion == 3:
            Obj.modificar()
        elif opcion == 4:
            Obj.venta()