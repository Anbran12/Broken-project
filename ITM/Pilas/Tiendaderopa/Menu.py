import PuntoPrendas as PP
#import Punto1 as p1
#import Punto2 as p2
#import Punto3 as p3
#import Punto4 as p4
#import Punto5 as p5
#import Punto6 as p6
#import Punto7 as p7

while True:
    try:
        print("\nMenú:",
              "\n1. Tienda.")
        O = int(input("\nIngresa la opción que deseas ejecutar (1 - 11) o cero (0) para salir: "))
        if O in [1]:
            if O == 1:
                Objp1 = PP.Prendas()
                Objp1.prenda()
        elif O in [2,3,4,5,6,7,8,9,10,11]:
            print("En mantenimiento")
        elif O == 0:
            print("Saliendo...")
            break
        else:
            print("Opción no valida")
    except ValueError:
        print("Error: Debe ingresar un número")