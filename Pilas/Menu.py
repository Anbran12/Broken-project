import PuntoVehiculos as p1
#import Punto1 as p1
#import Punto2 as p2
import Punto3 as p3
#import Punto4 as p4
#import Punto5 as p5
#import Punto6 as p6
#import Punto7 as p7

while True:
    try:
        print("\nMenú:",
              "\n3. Punto 3.",
            "\n10. Llenar datos vehiculos.")
        O = int(input("\nIngresa la opción que deseas ejecutar (1 - 10) o cero (0) para salir: "))
        if O in [3,10]:
            if O == 3:
                Objp3 = p3.Punto3()
                Objp3.punto3()
            if O == 10:
                Objp10 = p1.PuntoVehiculos()
                Objp10.puntovehiculos()
        elif O in [1,2,3,4,5,6,7,8,9]:
            print("En mantenimiento")
        elif O == 0:
            print("Saliendo...")
            break
        else:
            print("Opción no valida")
    except ValueError:
        print("Error: Debe ingresar un número")