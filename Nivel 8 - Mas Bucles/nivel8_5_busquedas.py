# BÚSQUEDAS y CONTAR ELEMENTOS EN LISTAS

"""
Programa que comprueba cuantas veces está un número
en una lista dada
"""

lista = [28, 36, 43, 52, 61, 43, 75, 84, 43, 97, 43]
numero = 43
repeticiones = 0
for i in lista:
    if i == numero:
        repeticiones += 1
print(f"El numero {numero} se repite {repeticiones} veces")




