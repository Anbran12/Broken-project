while True:
    try:
        opcion = int(input("Ingresa la opción a validar: "))
        if opcion in [1,2,3]:
            break
        else:
            print("Opción no valida.")
    except ValueError:
        print("Ingresa un valor tipo numerico")
        
print("Ok")