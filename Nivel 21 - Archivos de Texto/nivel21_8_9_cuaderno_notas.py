"""
Vamos acrear un programa para crear notas.
1º creamos un arch1vo (notas) donde guardamos el nombre de todas las notas.
luego un archivo por nota.
dos notas no podrán tener el mismo nombre.
Al ser un programa corto, no se usan funciones.

-----------------------------------
        CUADERNO DE NOTAS
-----------------------------------
------------  NOTAS ---------------
----------- OPCIONES --------------
1. Crear nueva nota
2. Leer una nota
3. Cambiar nombre nota
4. Borrar nota
5. Salir
-----------------------------------


En esta parte haremos los 2 primeros apartados.

"""

import os

# 1º comprobamos si el archivo notas existe. Si no, lo creamos
if not os.path.exists("notas.txt"):
        with open("notas.txt", "w") as archivo_notas:
                pass
        
while True:
        os.system("cls")
        # abrimos el archivo para ver los nombres
        with open("notas.txt", "r") as archivo_notas:
                # leemos las lineas y creamos una lista con todas las notas
                lista_notas = archivo_notas.readlines()
                
        for i in range(len(lista_notas)):
                # quitamos los espacios y los saltos de linea
                lista_notas[i] = lista_notas[i].strip()
                
        # ponemos cabecera
        print("-----------------------------------")
        print("        CUADERNO DE NOTAS")
        print("------------  NOTAS ---------------")
        
        if len(lista_notas) == 0:
                print("No hay notas ")
        else:
                n = 0
                for nota in lista_notas:
                        n += 1
                        print(f"Nota {n}: {nota}")
                # esto sería mas eficiente con enumerate
                # for n, nota in enumerate(lista_notas, 1):
                #         print(f"Nota {n}: {nota}")
                
        # creamos el menú
        print("----------- OPCIONES --------------")
        print("1. Crear nueva nota")
        print("2. Leer una nota")
        print("3. Cambiar una nota")
        print("4. Borrar nota")
        print("5. Salir")
        print("-----------------------------------")
        
        opcion = ""
        while opcion not in ("1", "2", "3", "4", "5"):
                opcion = input("--> ") 
                
        if opcion == "1":
                # pedimos el nombre
                nombre = input("Nombre de nota: ").strip()
                # ... y comprobamos si ya existe
                if os.path.exists(nombre + ".txt"):
                        print("Ese nombre ya existe.")
                        print()
                        input("Enter para continuar...")
                else:
                        # abrimos el archivo para añadir al final (a) el nombre de la nueva nota
                        with open("notas.txt", "a") as archivo_notas:
                                archivo_notas.write(nombre + "\n")
                        # abrimos otro archivo en modo escritura (al fnial (w)) para guardar el contenido
                        with open(nombre + ".txt", "w") as nuevo_archivo:
                                while True:
                                        print("Escribe contenido ('q' para salir)")
                                        contenido = input("> ")
                                        if contenido == 'q':
                                                break
                                        else:
                                                nuevo_archivo.write(contenido + "\n")
        
        elif opcion == "2":
                numero = input("Numero de nota: ")
                numeros_posibles = []
                # iteramos por la cantidad de notas desde el 1
                for i in range(1, len(lista_notas) + 1):
                        numeros_posibles.append(str(i))
                if numero not in numeros_posibles:
                        print("Numero de nota incorrecto.")
                        print()
                        input("Enter para continuar...")
                else:
                        numero = int(numero)
                        nota = lista_notas[numero-1]
                        with open(nota + ".txt", "r") as archivo_nota_leer:
                                contenido_nota = archivo_nota_leer.read()
                        print("-----------------------------------")
                        print()
                        print(contenido_nota)
                        print("-----------------------------------")
                        input("Enter para continuar...")
                        
        
        elif opcion == "5":
                break

