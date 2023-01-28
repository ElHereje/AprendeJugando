'''

Convertir un diccionario en 2 listas
pares = {"A":1, "B":2, "C":3, "D":4, "E":5}

Convertir dos listas en un diccionario
letras = ["A", "B", "C", "D", "E"]
numeros = [1, 2, 3, 4, 5]

Para llevarlo a cabo es conveniente crear un diccionario vacío
d = {}   manera 1
f = dict()   manera 2

'''

# # para el primero, creamos 1º dos listas vacías donde guardar los valores
# letras = []
# num = []
# pares = {"A":1, "B":2, "C":3, "D":4, "E":5}
# #
# # for clave in pares:
# #     letras.append(clave)
# #     num.append(pares[clave])
# #
# # Otra manera:
# for clave, valor in pares.items():
#     letras.append(clave)
#     num.append(valor)
# otra manera mas...
# letras = list(pares.keys())
# num = list(pares.values())
#
# print(letras)
# print(num)

# Para el 2º
letras = ["A", "B", "C", "D", "E"]
numeros = [1, 2, 3, 4, 5]

# Manera 1
# bucle for
# dicc = {}
# for i in range(len(letras)):
#   dicc[letras[i]] = numeros[i]
#
# print(dicc)

# manera 2
# usamos los métodos dict() para crearlo y zip() para fusionar los valores
dicc = dict(zip(letras, numeros))
print(dicc)
