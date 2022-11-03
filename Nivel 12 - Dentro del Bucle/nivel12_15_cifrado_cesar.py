"""
Este cifrado consiste en desplazar cada letra n posiciones, donde n es la
clave de cifrado.
Este cifrado es muy simple, y puede resolverse incluso son la clave
"""

alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
mensaje = "Este mensaje es secreto."
clave = 7

cifrado = ""

# vamos a ir buscando el índice de cada letra, ya ese índice le sumamos la
# clave y buscamos en el alfabeto la letra resultante.
# Cuando lleguemos al final del alfabeto, se sigue por el principio, con lo
# cual, si llegamos al índice 27, lo que hacemos es restarle el nº de letras,
# que son 27


for letra in mensaje.upper():
    if letra in alfabeto: # nos aseguramos que ese carácter está en el alfabeto
        indice = alfabeto.find(letra)
        indice += clave
        if indice >= 27:
            indice -= 27
        cifrado += alfabeto[indice]
    else: # si ese carácter no está en el alfabeto, se deja tal cual
            # como pueden ser los espacios o puntos
        cifrado += letra
print(cifrado)


