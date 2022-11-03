"""
Programa que administra una lista de la compra.
Vamos a empezar a diseñar el programa antes de codificar:

----- PROGRAMA: LISTA DE LA COMPRA -----

1. Mostrar mensaje de presentación.
2. Mostrar menú de opciones: pedir una.
    Añadir, Eliminar, Mostrar, Salir
3. Opción Añadir: Pide nombre del producto.
    Si ya está indicarlo, si no añadirlo
4. Eliminar: Pide nombre del producto.
    Si no está indicarlo, si nó eliminarlo.
5. Mostrar muestra la lista completa.
6. Salir sale del programa.
7. Opción incorrecta indicarlo.
8. Volver al menú tras cada acción hasta que se salga

"""

compra = []
opc = None
print(" ----- LISTA DE LA COMPRA -----")
while True:
    print()
    print("Opciones disponibles: ")
    print()
    print("1. Añadir producto a la lista.")
    print("2. Eliminar producto de la lista.")
    print("3. Mostrar lista de la compra.")
    print("4. Salir del programa")
    print()
    opc = input("Elige una de las opciones: ")
    print()
    if opc == "1":
        nuevo = input("¿Que producto añadimos?: ")
        if nuevo in compra:
            print("Ese producto ya se encuentra en la lista...")
            nuevo = input("¿Que producto añadimos?: ")
            compra.append(nuevo)
        else:
            compra.append(nuevo)
    elif opc == "2":
        print(compra)
        print()
        elimina = input("¿Que producto eliminamos?: ")
        if elimina not in compra:
            print("Ese artículo no se encuentra en la lista.")
            print("Seleccione un correcto a eliminar.")
            elimina = input("¿Que producto eliminamos?")
            compra.remove(elimina)
        else:
            compra.remove(elimina)
    elif opc == "3":
        print(compra)
    elif opc == "4":
        break
    else:
        print("Opcion incorrecta, inténtalo de nuevo")
        print()