'''
Tenemos una lista con nombres, algunos con minúsculas y otros con mayúsculas:

datos = ["Sara", "marta", "Daniel", "roberto"]

Y queremos hallar otra lista con los nombres que estén con todas las letras en minúsculas,
excepto la última que esté en mayúsculas

hacerlo con map y por comprension

'''

datos = ["Sara", "marta", "Daniel", "roberto"]

nombres = list(map(lambda x: x[:-1].lower() + x[-1].upper(), datos))
print(nombres)

nombres2 = [x[:-1].lower() + x[-1].upper() for x in datos]
print(nombres2)

''' 
Restar los elementos de una lista de los elementos
con el mismo índice de la otra
'''

primera = [7, 9, 6, 8, 5]
segunda = [3, 2, 1, 5, 4]

totales = [x-y for x, y in zip(primera, segunda)]
print(totales)

totales2 = list(map(lambda x, y: x-y, primera, segunda))
print(totales2)


'''
Crear lista de diccionarios a partir de lista de tuplas.
Las claves serán: "Nombre", "Peso", "Precio",
y los valores los elementos de las tuplas
'''

metales = [("Hierro", 415, 12), ("Cobre", 158, 32), ("Zinc", 243, 21)]

# con map

metales2 = list(map(lambda x: {"Nombre": x[0], "Peso": x[1], "Precio": x[2]}, metales))
for elemento in metales2:
    print(elemento)

# por comprension

metales3 = [{"Nombre": x[0], "Peso": x[1], "Precio": x[2]} for x in metales]
for elemento in metales3:
    print(elemento)