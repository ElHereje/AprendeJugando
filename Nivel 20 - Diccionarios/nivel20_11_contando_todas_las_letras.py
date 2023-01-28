'''
parecido al 20_7, pero incluyendo todas las letras del alfabeto
que no aparecen
'''

frase = "Hoy ha salido el sol y hace una mañana estupenda"
alfabeto = "abcdefghijklmnñopqrstuvwxyzáéíóúü .,"

# inicializamos un diccionario con valores 0 desde el alfabeto
conteo = dict.fromkeys(alfabeto, 0)

# creamos el bucle que cuente las letras
for letra in frase.lower():
    if letra in conteo:
        conteo[letra] += 1
# imprimimos el resultado (el diccionario creado)
for le, nu in conteo.items():
    print(f"{le}: {nu}")