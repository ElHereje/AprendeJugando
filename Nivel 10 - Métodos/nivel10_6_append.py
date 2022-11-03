"""
Programa que crea una lista con 100 elementos, que son los numeros
del 1 al 100
"""

lista = []

for num in range(1, 101):
    lista.append(num)
print(lista)


"""
Tenemos una lista de numeros y queremos separar
los pares de los impares y guardarlos en otras 2 listas.
"""

numeros = [2,3, 5, 8, 9, 12, 21, 24, 25, 28]
pares = []
impares = []

for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print(numeros)
print(pares)
print(impares)
