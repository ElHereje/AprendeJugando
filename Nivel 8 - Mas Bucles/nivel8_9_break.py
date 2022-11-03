# USO DEL BREAK

"""
Programa que comprueba si un número  está
dentro de una secuencia
"""

numero = 20
secuencia = range(1, 10000)
for i in secuencia:
    if i == numero:
        print(f"tenemos el nº en la posición {i}")
        break
    else:
        print(f"Posición {i} --> No tá")



