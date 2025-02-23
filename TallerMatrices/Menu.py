import Punto1 as p1
import Punto2 as p2
import Punto3 as p3
import Punto4 as p4
import Punto5 as p5
import Punto6 as p6
import Punto7 as p7

while True:
    try:
        print("\nMenú:",
            "\n1. Suma total de la matriz.",
            "\n2. Número mayor en la matriz.",
            "\n3. Suma de filas y columnas.", 
            "\n4. Mayor suma de columna.",
            "\n5. Matriz almacenada en vector.",
            "\n6. Suma de filas y columnas en vector.", 
            "\n7. Positivos y negativos en la matriz.")
        O = int(input("\nIngresa la opción que deseas ejecutar (1 - 10) o cero (0) para salir: "))
        if O in [1,2,3,4,5,6,7]:
            if O == 1:
                Objp1 = p1.P1()
                Objp1.p1()
            elif O == 2:
                Objp2 = p2.P2()
                Objp2.p2()            
            elif O == 3:
                Objp3 = p3.P3()
                Objp3.p3()                
            elif O == 4:
                Objp4 = p4.P4()
                Objp4.p4()
            elif O == 5:
                Objp5 = p5.P5()
                Objp5.p5()
            elif O == 6:
                Objp6 = p6.P6()
                Objp6.p6()
            elif O == 7:
                Objp7 = p7.P7()
                Objp7.p7()
        elif O in [8,9,10]:
            print("En mantenimiento")
        elif O == 0:
            print("Saliendo...")
            break
        else:
            print("Opción no valida")
    except ValueError:
        print("Error: Debe ingresar un número")