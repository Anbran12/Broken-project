# MENU PRINCIPAL
import Punto1 as p1
import Punto2 as p2
import Punto3 as p3

while True:
    try:
        opcion = int(input("\nIngrese el punto a ejecutar (1 - 10): "))
        if opcion in [1,2,3]:   
            if opcion == 1:
                #PUNTO 1
                punto1 = p1.Punto1()
                print(punto1.Epunto1())

            if opcion == 2:
                #PUNTO 2
                punto2 = p2.Punto2()
                print(punto2.Epunto2())

            if opcion == 3:
                #PUNTO 3
                punto3 = p3.Punto3()
                print(punto3.Epunto3())
        
        if opcion in [4,5,6,7,8,9,10]:
            print("\nEn mantenimiento")

        else:
            print("\nOpción no valida")
    except ValueError:
        print("\nIngresa un valor tipo numerico.")