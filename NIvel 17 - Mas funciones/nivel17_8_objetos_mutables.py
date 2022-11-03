"""
Debemos tener cuidados al definir funciones que tomen como parámetros
objetos mutables, como las listas, ya que las podemos modificar
"""
def calcula_media(lista1, lista2):
    lista1.extend(lista2)
    return sum(lista1) / len(lista1)

notas1 = [5, 6, 9]
notas2 = [4, 7, 8]

nota_media = calcula_media(notas1, notas2)
print(nota_media)

# con esto, hemos modificado la lista notas1. Si no queremos que se
# modifique, tendremos que desechar el extend...:

def calcula_media2(lista1, lista2):
    total = lista1 + lista2
    return sum(total) / len(total)

notas1 = [5, 6, 9]
notas2 = [4, 7, 8]

nota_media = calcula_media2(notas1, notas2)
print(nota_media)


# Otro ejemplo podría ser:

def mejores_3_notas(lista):
    lista.sort(reverse = True)
    return lista[0:3]   # ¡Esto hace que se modifique la lista !!!!!

notas = [3, 5, 8, 6, 2, 9, 4, 7]
print(mejores_3_notas(notas))

# Para solventar esto, podemos copiar la lista:
def mejores_3_notas_b(lista):
    copia = list(lista)
    copia.sort(reverse = True)
    return copia[0:3]   # ¡Esto hace que se modifique la lista !!!!!

notas = [3, 5, 8, 6, 2, 9, 4, 7]
print(mejores_3_notas_b(notas))