'''
Este método permite inicialiar un diccionario a partir
de un iterable(listas, cadenas, range,...
'''

# ejemplo: queremos crear un diccionario a partir de esta lista

minerales = ["Pirita", "Topacio", "Cinabrio", "Obsidiana",
             "Manganita", "Alabastro", "Turquesa", "Galena"]

# 1º necesitamos un diccionario vacío sobre el que usamos el método:
# coleccion = {}.fromkeys(minerales, 0)  # (mineral: cantidad)
coleccion = dict.fromkeys(minerales, 0)  # (mineral: cantidad)

print(coleccion)

# en vez de lista también puede ser un range
numeros = dict.fromkeys(range(100,111), 50)
print(numeros)