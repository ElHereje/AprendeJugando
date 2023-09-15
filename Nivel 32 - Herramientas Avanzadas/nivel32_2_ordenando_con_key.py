'''
RETO:
datos = [(4, 2, 1), (5, 4, 2), (2, 1, 3), (3, 0, 1), (3, 4, 2)]

1 - Ordenar de menor a mayor según la suma de sus elementos
2 - Ordenar de menor a mayor teniendo en cuenta el elemento 3, desp el 2 y luego el 1

'''

datos = [(4, 2, 1), (5, 4, 2), (2, 1, 3), (3, 0, 1), (3, 4, 2)]

# para el uno, podemos hacerlo de 2 maneras:
print(sorted(datos, key=sum)) # [(3, 0, 1), (2, 1, 3), (4, 2, 1), (3, 4, 2), (5, 4, 2)]
datos.sort(key=sum) # no devuelve nada, sino que ordena la propia lista
print(datos) # [(3, 0, 1), (2, 1, 3), (4, 2, 1), (3, 4, 2), (5, 4, 2)]


# para el segundo caso, volvemos a desordenar la lista:
datos = [(4, 2, 1), (5, 4, 2), (2, 1, 3), (3, 0, 1), (3, 4, 2)]

def reverso(tupla):
    return (tupla[2], tupla[1], tupla[0])

print(sorted(datos, key=reverso)) # [(3, 0, 1), (4, 2, 1), (3, 4, 2), (5, 4, 2), (2, 1, 3)]


# PARA ESTOS CASOS, EN LOS QUE HAY QUE CREAR UNA FUNC. ESPECÍFICA, EXISTEN LAS 
# FUNCIONES LAMBDA, QUE SE VERÁN EN EL SIGUIENTE VIDEO
