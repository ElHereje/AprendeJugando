"""
Programa que pide datos (tratamiento, nombre y apellido) de las personas
que han sido invitadas a una fiesta, para enviarles una carta de invitación.
Luego se muestra en pantalla la carta con los datos que se piden,
y se pregunta si se quiere introducir nuevos datos de otra person:

MODELO DE CARTA

Introduzca los datos de la persona:
Tratamiento (Sr/Sra): sr
Nombre: andrés
Apellido: Sanchez

Sr. Andrés Sanchez:
Le escribo para informarle
de que ha sido usted invitado
a la fiesta de la Empresa
Atentamente.

¿Desea imprimir otra carta (s/n)?:

"""

# Modelo 1
'''print("MODELO DE CARTA")

salida = True

while salida:
    print("Introduzca los datos de la persona: ")
    tratamiento = input("Tratamiento (Sr/Sra):")
    nombre = input("Nombre: ")
    ape = input("Apellido: ")

    if tratamiento.lower() == "sr":
        print(f"""Sr. {nombre.capitalize()} {ape.capitalize()}:
                  Le escribo para informarle
                  de que ha sido usted invitado
                  a la fiesta de la Empresa.
                  Atentamente.\n""")
    elif tratamiento.lower() == "sra":
        print(f"""Sra. {nombre.capitalize()} {ape.capitalize()}:
                  Le escribo para informarle
                  de que ha sido usted invitada
                  a la fiesta de la Empresa.
                  Atentamente.\n""")

    if input("¿Desea imprimir otra carta (s/n)?:") != "s":
        break'''


# Modelo 2
print("MODELO DE CARTA\n")

while True:
    print("Introduzca los datos de la persona: ")
    tratamiento = input("Tratamiento (Sr/Sra): ")
    nombre = input("Nombre: ")
    ape = input("Apellido: ")
    print(f"{tratamiento.title()} {nombre.title()} {ape.title()}: ")
    # print("{} {} {}: ".format(tratamiento.title(), nombre.title(),ape.title()))
    print("Le escribo para informarle")
    if tratamiento.lower() == "sr":
        print("de que ha sido usted invitado")
    elif tratamiento.lower() == "sra":
        print("de que ha sido usted invitada")
    print("a la fiesta de la Empresa.")
    print("Atentamente.\n")

    seguir = input("¿Desea imprimir otra carta (s/n)?: ")
    if seguir.lower() == "n":
        break
