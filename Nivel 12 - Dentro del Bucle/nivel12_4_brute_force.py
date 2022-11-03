# Búsqueda por fuerza fruta es buscar todas las posible combinaciones.
# (por ejemplo, candado con 3 ruedas de 10 números cada una --> 1000 combinaciones)
# en este caso, serían variaciones con combinaciones de 10 números tomados
# de 3 en 3

"""
Programa que muestra todas las posibles combinaciones
para poder abrir un candado de clave de tres ruedas.
"""

'''for i in range(10):
    for j in range(10):
        for k in range(10):
            combinacion = str(i) + str(j) + str(k)
            print(combinacion)'''


# Para un candado de 4 ruedas:

for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                combinacion = str(i) + str(j) + str(k) + str(l)
                print(combinacion)
