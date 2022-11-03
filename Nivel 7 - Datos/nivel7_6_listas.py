# LISTAS

# siempre van entre corchetes
# SON MODIFICABLES

mascotas = ["gato", "perro", "canario", "cocodrilo"]
print(mascotas)

mascotas[3] = "tortuga"
print(mascotas)

mi_lista= []
mi_lista += [1, 2, 3]
print(mi_lista) # --> [1, 2, 3]
mi_lista = mi_lista * 3
print(mi_lista) # --> [1, 2, 3, 1, 2, 3, 1, 2, 3]

'''
Crea una lista que contenga los nº del 1 al 100 usando un 
bucle while y partiendo de una lista vacía
'''

lista = []
contador = 1
while contador <= 100:
    lista += [contador]
    contador += 1
print(lista)

