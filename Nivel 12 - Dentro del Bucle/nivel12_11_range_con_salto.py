# Vamos a recordar el tipo range y, en concreto, el tercer argumento
# que es el salto entre datos


'''intervalo = range(10)   # rango del 0 al 9

for i in intervalo:
    print(i)'''

'''# para ir del 1 al 10:
for i in range(1, 11):
    print(i)'''

# si en el salto no indicamos nada, se entiende que es 1
'''for i in range(1, 11, 2):
    print(i)  # --> del 1 al 10 de 2 en 2
print()'''

# también puede ser a la inversa:
'''for i in range(10, -1, -1):
    print(i)  # --> del 10 al 1 (por eso el 2º es -1)'''

# con range también podemos crear listas:
'''lista = list(range(1, 101))
print(lista)'''

# una de las ventajas de usar range con una lista:
# (veremos el espacio en bytes)
import sys

intervalo = range(1, 1001)
lista = list(range(1, 1001))

bytes_intervalo = sys.getsizeof(intervalo)
bytes_lista = sys.getsizeof(lista)

print(bytes_intervalo)  # --> 48
print(bytes_lista)  # --> 856  mucho mas espacio ocupado

# a la hora de crear una secuenia de nº enteros, conviene hacerlo
# con un intervalo range

