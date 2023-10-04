frutas = ["manzana", "naranja", "platano", "pera", "melón"]

# imaginemos que queremos asignar un nº a cada elemento de la lista o 
# saber cual es su índice

for elementos in enumerate(frutas, 1): # el 1 es para que comience con ese nº
    print(elementos)
    '''
        (1, 'manzana')
        (2, 'naranja')
        (3, 'platano')
        (4, 'pera')   
        (5, 'melón') 
    '''

# podemos crear otras listas...

numerados = list(enumerate(frutas))
# esto devuelve un iterador, que guardamos en "numerados"

print(numerados) # [(0, 'manzana'), (1, 'naranja'), (2, 'platano'), (3, 'pera'), (4, 'melón')]

# tb podemos crear listas por comperensión:

num = [[x, y] for x, y in enumerate(frutas)]
print(num) # [[0, 'manzana'], [1, 'naranja'], [2, 'platano'], [3, 'pera'], [4, 'melón']]


# tb podemos convertirlo en un diccionario:
nume = dict(enumerate(frutas))
print(nume) # {0: 'manzana', 1: 'naranja', 2: 'platano', 3: 'pera', 4: 'melón'}

# esto se puede aplicar tab a cadenas de caracteres....

for indice, letra in enumerate("artefacto"):
    print(indice, letra)
    '''
    0 a
    1 r
    2 t
    3 e
    4 f
    5 a
    6 c
    7 t
    8 o
    '''
# imaginemos un matriz:

matriz = [
    [0,0,0,0,0,1,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,1,0],
    [0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0]
]
# queremos una lista con el índice donde esta el 1 de cada una de las filas
unos = [i for fila in matriz for i, v in enumerate(fila) if v == 1]
print(unos) # --> [5, 2, 4, 6, 7, 0, 3]

'''
RETO

Dada una lista:

datos = [43, 27, 58, 12, 39, 58, 54, 33, 21, 58, 17, 46]

1. Hallar el índice de la primera coincidencia del número mayor
2. Hallar los índices de todas las coincidencias del número mayor
'''