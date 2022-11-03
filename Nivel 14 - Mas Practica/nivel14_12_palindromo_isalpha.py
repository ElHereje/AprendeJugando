"""
Ejercicio: programa que verifique si una frase o palabra
es un palíndromo
Realizarlo usando isalpha()
"""

cadena = '''
Allí por la tropa portado, traído a ese paraje
de maniobras, una tipa como capitán usar boina
me dejará, pese a odiar toda tropa por tal ropilla
'''

# pasamos a minúsculas
minus = cadena.lower()

# quitamos espacios, comas y puntos
cadena_plana = ""
for letra in minus:
    if letra.isalpha():
        cadena_plana += letra

# quitamos las tildes
cadena_final = cadena_plana.replace("á", "a").replace("é", "e")\
    .replace("í", "i").replace("ó", "o").replace("ú", "u")

# revertimos la cadena
reverso = cadena_final[::-1]

# comprobamos si es o no palíndromo
if cadena_final == reverso:
    print("Son PALÍNDROMOS")
else:
    print("NO son PALÍNDROMOS")
