"""
Imagina uin mensaje cifrado con "cifrado cesar" y el alfabeto es el
de 27 letras del castellano, pero no se sabe la clave.
¿Cual sería el mensaje?

Se hará en dos pasos:
    1. sabiendo la clave (7 y mensaje igual que el ejercicio anterior)
    2. por "fuerza bruta" usar dicho programa para descifrarlo sin clave
"""

# Punto 1 - CON CLAVE
'''cifrado = "LZAL SLTZHPL LZ ZLJYLAV."
clave = 7
alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
mensaje = ""

for letra in cifrado.upper():
    if letra in alfabeto: # buscamos el índice
        indice = alfabeto.index(letra)
        indice -= clave
        if indice < 0: # bajamos de la A..."
            indice += 27
        mensaje += alfabeto[indice]
    else:
        mensaje += letra
print(mensaje)'''

# Punto 2 - SIN CLAVE

cifrado = "BDARDMXMD PY BKFSAY PE ÑAXA GY UGPRA"
alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# En este caso, por fuerza bruta, probamos todas las claves posible,
# es decir, de la 1 a la 26 ( la 0 o 27 darían el mensaje original), y por
# el resto, reutilizamos el código anterior:

for clave in range(len(alfabeto)):
    mensaje = ""
    for letra in cifrado.upper():
        if letra in alfabeto:  # buscamos el índice
            indice = alfabeto.index(letra)
            indice -= clave
            if indice < 0:  # bajamos de la A..."
                indice += 27
            mensaje += alfabeto[indice]
        else:
            mensaje += letra
    print(f"Clave: {clave} - {mensaje} ")


