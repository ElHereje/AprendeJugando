# PRÁCTICA CON BREAK

"""
Tenemos una lista de temperaturas. Hay que comprobar que todas las
temperaturas están entre 18 y 25 incluidos.
Si alguna no la cumple, se para el programa y lo indica, si no va
mostrando que la temperatura verificada es correcta.
"""

temperaturas = [19, 22, 21, 24, 23, 27, 21, 20, 19, 18, 21, 20]

for i in range(len(temperaturas)):
    if not 18 <= temperaturas[i] <= 25:
        print(f"Temperatura fuera de rango en posición {i + 1}  --> {temperaturas[i]}º")
        break
    else:
        print(f"Correcta")
print("Fin del programa")

# ******************************************************


"""
programa que pida adivinar un número del 1 al 10.
cuando lo divinas, se para.
Usar un break en vez de bandera
"""

numero = 5

while True:
    intento = int(input("Dime un nº del 1 al 10: "))
    if intento == numero:
        print("Has acertado")
        break
    else:
        print("No has acertado. Sigue intentando.")


# ***********************************
