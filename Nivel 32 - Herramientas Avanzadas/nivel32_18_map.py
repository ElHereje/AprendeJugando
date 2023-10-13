datos = [3, 4, 5, 6, 7]

'''
La función map toma como argumentos otra función y uno o varios iterables. 
Pasa esa función a todos los elementos de esos iterables
'''

dobles = list(map(lambda x: x*2, datos))
print(dobles) # --> [6, 8, 10, 12, 14]

# esto habría sido mas sencillo por lsitas por comprensión
dobles2 = [x*2 for x in datos]
print(dobles2)

# convertir en entoros una cadenas:
cadenas = ["1", "2", "3", "4", "5"]
numeros = list(map(int, cadenas))
print(numeros)
# por compresion
numeros2 = [int(x) for x in cadenas]
print(numeros2)

'''
RETO
Tenemos una lista con nombres, algunos con minúsculas y otros con mayúsculas:

datos = ["Sara", "marta", "Daniel", "roberto"]

Y queremos hallar otra lista con los nombres que estén con todas las letras en minúsculas, 
excepto la última que esté en mayúsculas

'''