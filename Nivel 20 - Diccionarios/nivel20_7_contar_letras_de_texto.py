'''
Contador de letras:Programa que cuenta la cantidad
de cada una de las letras que aparecen en una frase.
'''

frase = "Hoy ha salido el sol y hace una mañana estupenda"

# primero creamos un diccionario vacío
conteo = {}

# ahora vamos añadiendo parejas de cada letra y su cantidad
for letra in frase.lower():
    if letra not in conteo:
        conteo[letra] = 1
    else:
        conteo[letra] += 1

# para presentar el diccionario
for k, v in conteo.items():
    print(f"Letra {k}: {v} veces")