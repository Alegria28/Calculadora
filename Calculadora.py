while (True):
    print("Presiona un numero para proceder: ")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = int(input("- "))
    if opcion == 1:
        print("Escriba los numeros que quiere sumar")
        num1 = int(input("--> "))
        num2 = int(input("--> "))
        print("La suma es:", num1 + num2)
        print("-------------------------")
    elif opcion == 2:
        print("Escriba los numeros que quiere restar")
        num1 = int(input("--> "))
        num2 = int(input("--> "))
        print("La resta es:", num1 - num2)
        print("-------------------------")
    elif opcion == 3:
        print("Escriba los numeros que quiere multiplicar")
        num1 = int(input("--> "))
        num2 = int(input("--> "))
        print("La multiplicacion es:", num1 * num2)
        print("-------------------------")
    elif opcion == 4:
        print("Escriba los numeros que quiere dividir")
        num1 = int(input("--> "))
        num2 = int(input("--> "))
        print("La divicion es:", num1 // num2)
        print("-------------------------")
    elif opcion == 5:
        print("Adios")
        break
    else:
        print("Debe de ser un numero entre 1 y 5")
        print("-------------------------")