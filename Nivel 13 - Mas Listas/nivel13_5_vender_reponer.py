# mejoramos rl programa anterior con un menú

cajonera = [
                [
                 [["A", 18], ["B", 21],  ["C", 11], ["D", 10], ["E", 8]],
                 [["F", 25], ["G", 18],  ["H", 18], ["I", 16],  ["J", 32]],
                 [["K", 21], ["L", 54], ["M", 11], ["N", 18], ["Ñ", 10]]
                  ],
                 [
                [["O", 18], ["P", 21], ["Q", 11], ["R", 10], ["S", 8]],
                [["T", 25], ["U", 18], ["V", 18], ["W", 16], ["X", 32]],
                [["Y", 21], ["Z", 54], [" ", 0], [" ", 0], [" ", 0]]
                 ]
                ]

while True:
    print()
    print("1. Mostrar Inventario.")
    print("2. Venta de letra.")
    print("3. Reposición de letra.")
    print("4. Salir.")
    opcion = input("--> ")

    if opcion == "1":
        print()
        print("Cajonera".center(50))
        print()
        for cajon in cajonera:
            for fila in cajon:
                for espacio in fila:
                    print(f"{espacio[0]} : {espacio[1]}      ", end="")
                print()
            print()

    elif opcion == "2":
        letra = input("Introduce letra a vender:  ").upper()
        cantidad = int(input("Introduce cantidad:  "))
        for cajon in cajonera:
            for fila in cajon:
                for espacio in fila:
                    if espacio[0] == letra:
                        espacio[1] -= cantidad

    elif opcion == "3":
        letra = input("Introduce letra a vender:  ").upper()
        cantidad = int(input("Introduce cantidad:  "))
        for cajon in cajonera:
            for fila in cajon:
                for espacio in fila:
                    if espacio[0] == letra:
                        espacio[1] += cantidad

    elif opcion == 4:
        break

    else:
        print("Introduce opción correcta.....")
