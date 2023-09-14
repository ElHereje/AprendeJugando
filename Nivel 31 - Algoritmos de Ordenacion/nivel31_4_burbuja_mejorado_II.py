'''
este sigue siendo ineficiente en comparación con otros ordenamientos sencillos de 
complejidad cuadrática (como el ya visto "por seleccion").
Vamos a verlo
'''

import random

#creamos una lista por comprensión:
lista = [random.randint(1, 100) for n in range(100)] # 100 nºs aleatorios del 1 al 100

# hacemos 4 copias
lista2 = list(lista)
lista3 = list(lista)
lista4 = list(lista)
lista5 = list(lista)

print("-----------------------------------------------")

# algoritmo básico de burbuja:
comparaciones = 0
cambios = 0

for i in range(len(lista)-1): 
    for j in range(len(lista)-1): 
        comparaciones += 1
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j] 
            cambios += 1
print(lista)
print(f"Burbuja Básico. Comparaciones: {comparaciones}, Cambios: {cambios}")

print("-----------------------------------------------")

# algoritmo por reduccion:
comparaciones = 0
cambios = 0

for i in range(len(lista2)): 
    for j in range(len(lista2) - i -1): 
        comparaciones += 1
        if lista2[j] > lista2[j+1]:
            lista2[j], lista2[j+1] = lista2[j+1], lista2[j] 
            cambios += 1
print(lista2)
print(f"Con reducción. Comparaciones: {comparaciones}, Cambios: {cambios}")

print("-----------------------------------------------")

# algoritmo con centinela:
comparaciones = 0
cambios = 0
desordenada = True

while desordenada: 
    desordenada = False
    for j in range(len(lista3) -1): 
        comparaciones += 1
        if lista3[j] > lista3[j+1]:
            lista3[j], lista3[j+1] = lista3[j+1], lista3[j] 
            cambios += 1
            desordenada = True

print(lista3)
print(f"Con centinela. Comparaciones: {comparaciones}, Cambios: {cambios}")

print("-----------------------------------------------")

# algoritmo con centinela y reducción:
comparaciones = 0
cambios = 0
desordenada = True
i = 0

while desordenada and i < len(lista4) - 1: 
    desordenada = False
    for j in range(len(lista4) -1 - i): 
        comparaciones += 1
        if lista4[j] > lista4[j+1]:
            lista4[j], lista4[j+1] = lista4[j+1], lista4[j] 
            cambios += 1
            desordenada = True
    i += 1

print(lista4)
print(f"Con centinela y reducción. Comparaciones: {comparaciones}, Cambios: {cambios}")

print("-----------------------------------------------")

# algoritmo por selección:
comparaciones = 0
cambios_lista = 0
cambios_variable = 0

for i in range(len(lista5) - 1):
    menor = i
    for j in range(i+1, len(lista5)): 
        comparaciones += 1
        if lista5[j] < lista5[menor]:
            menor = j
            cambios_variable += 1
    lista5[menor], lista5[i] = lista5[i], lista5[menor] 
    cambios_lista += 1

print(lista5)
print(f"Por Seleccion. Comparaciones: {comparaciones}")
print(f"Cambios de Variables: {cambios_variable}")
print(f"Cambios en la lista: {cambios_lista}")
