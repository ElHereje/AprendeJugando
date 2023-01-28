
# with open("notas/nota.txt", "w") as archivo:
#     archivo.write("Hola que tál..." + "\n")
#     archivo.write("... Hasta luego." + "\n")
#
# with open("notas/nota.txt", "r") as archivo:
#     texto = archivo.read()
#     print(texto)
#
# with open("notas/nota.txt", "a") as archivo:
#     archivo.write("Hola que tál 2..." + "\n")
#     archivo.write("... Hasta luego 2." + "\n")
#
# with open("notas/nota.txt", "r") as archivo:
#     texto = archivo.read()
#     print(texto)

with open("notas/nota.txt", "r+") as archivo:
    texto = archivo.read()
    print(texto)

    archivo.write("Hola que tál 4..." + "\n")
    archivo.write("... Hasta luego 4." + "\n")
    archivo.seek(0)
    texto = archivo.read()
    print(texto)
