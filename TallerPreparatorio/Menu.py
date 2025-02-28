import Punto1 as p1
import Punto2 as p2
import Punto3 as p3
import Punto5 as p5
import Punto6 as p6

while True:
    try:
        Opcion = int(input("\nIngresa una de las siguientes opciones (1 - 10): "))
        if Opcion in [1,2,3,5,6]:
            if Opcion == 1:
                P1 = p1.Punto1()
                P1.punto1()
            if Opcion == 2:
                P2 = p2.Punto2()
                P2.punto2()
            if Opcion == 3:
                P3 = p3.Punto3()
                P3.punto3()
            if Opcion == 5:
                P5 = p5.Punto5()
                P5.punto5()
            if Opcion == 6:
                P6 = p6.Punto6()
                P6.punto6()
        elif Opcion in [4,6,7,8,9,10]:
            print("En mantenimiento...")
        elif Opcion == 0:
            print("Saliendo...")
            break
        else:
            print("Opcion no valida.")
    except ValueError:
        print("\nEl valor ingresado no es valido.")              