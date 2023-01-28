
"""
Vamos a ver una forma más eficiente de hacer lo mismo que hasta ahora
se usa el método WITH
No hay que cerra el archivo, se hace solo al salir del with.
Vamos a trabajar también con rutas
"""

# with open("notas/nota1.txt", "r") as archivo:
#     texto = archivo.read()
#     print(texto)

# vamos a ver también como manejar errores
import os

if os.path.exists("notas/nota2.txt"):
    with open("notas/nota2.txt", "r") as archivo:
        texto = archivo.read()
        print(texto)
else:
    print("ESE ARCHIVO NO EXISTE")
