'''
RETO --> Lista con los pares de elementos de cantidades y aumentos, tales que
si sumamos una cantidad par mas un aumento impar o una cantidad impar mas un
aumento par tiene que dar 11

cantidades = [1, 4, 6, 7, 8]
aumentos = [2, 3, 4, 5, 6]

'''

cantidades = [1, 4, 6, 7, 8]
aumentos = [2, 3, 4, 5, 6]

parejas = [(c, a) for c in cantidades for a in aumentos
           if c % 2 == 0 and a % 2 != 0
           or c % 2 != 0 and a % 2 == 0
           if a + c == 11]
print(parejas)


# ---------------------------------------------------------------------------

# Aplanar lista (crear lista con los elementos de las sublistas)

lista = [[1, 2], [3, 4, 5, 6], [7, 8, 9]]

plana = [elemento for sublista in lista for elemento in sublista]
print(plana)