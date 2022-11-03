"""
POP es un método de las listas para eliminar elementos.
"""

# si no indicamos nada, pop elimina el último elemento de la lista:

lista = [1, 2, 3, 4, 5, 6, 7]
lista.pop()
print(lista)  # --> [1, 2, 3, 4, 5, 6].

# pop puede devolver el elemento afectado:
n = lista.pop()
print(n)  # --> 6

# se le puede añadir un índice:
m = lista.pop(0)
print(m)  # --> 1

