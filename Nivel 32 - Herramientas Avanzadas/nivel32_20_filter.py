
datos = [4, 3, -1, 9, 6, -5, 8, 7, 2]

# crear lista solo con los positivos
positivos = list(filter(lambda x: x>=0, datos))
print(positivos)

# solo los pares
pares = list(filter(lambda x: x%2==0, datos))
print(pares)

datos2 = [21, 0, 14, 0, 0, 27, 0, 0, 0, 19, 0, 32]

# quitar los ceros
numeros = list(filter(lambda x: x!=0, datos2))
numeros2 = list(filter(lambda x: x, datos2)) # el valor lógico de cero es FALSE
numeros3 = list(filter(bool, datos2)) # el valor lógico de cero es FALSE
numeros4 = list(filter(None, datos2)) # el valor lógico de cero es FALSE
print(numeros) # --> [21, 14, 27, 19, 32]
print(numeros2) # --> [21, 14, 27, 19, 32]
print(numeros3) # --> [21, 14, 27, 19, 32]
print(numeros4) # --> [21, 14, 27, 19, 32]

# ...con varios tipos de datos, queremos solo números
datos3 = [21, False, 0, 14, 0, None, 0, 27, 0, 0, 0, "", 19, 0, 32]
numeros5 = list(filter(None, datos3))
print(numeros5) # --> [21, 14, 27, 19, 32]


# si solo queremos quitar los None
datos4 = [21, None, 0, 14, 0, None, 0, 27, 0, 0, 0, 19, 0, 32]
numeros6 = list(filter(lambda x: x is not None, datos4))
print(numeros6) # --> [21, 0, 14, 0, 0, 27, 0, 0, 0, 19, 0, 32]


'''
Reto para resolver:

1. Crear una lista con metales con valor mayor i igual que 10.
2. Crear una lista con metales con valor mayor o igual que 10
   y que tengan "e" en su nombre.


metales = {
    "Hierro": "2",
    "Plata": "23",
    "Zinc": "7",
    "Cobre": "11",
    "Aluminio": "4",
    "Plomo": "15",
    "Oro": "30"
    }
'''