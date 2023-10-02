'''
RETO --> ordenra la lista por nombres en orden alfabético,
empezando por la m, usando un diccionario

nombres = ["Jorge", "Íñigo", "Alba", "María", "Cesar",
            "Marta", "Claudia", "Álvaro", "Paula", "Javier",
            "Silvia", "Ñuflo", "Azucena", "Irene", "Laura",
            "Zaira", "Añua", "Raúl", "Víctor", "Mario"] 
'''

nombres = ["Jorge", "Íñigo", "Alba", "María", "Cesar",
            "Marta", "Claudia", "Álvaro", "Paula", "Javier",
            "Silvia", "Ñuflo", "Azucena", "Irene", "Laura",
            "Zaira", "Añua", "Raúl", "Víctor", "Mario"] 

def ord_alf(cadena):  # nos va a dar el orden de cada una de las letras de cada palabra

    alfabeto = {
        "A":1, "Á":1, "a":1, "á":1,
        "B":3, "b":2,
        "C":4, "c":3,
        "D":5, "d":4,
        "E":6, "É":5, "e":1, "é":1,
        "F":7, "f":6,
        "G":8, "g":7,
        "H":8, "h":8,
        "I":9, "Í":9, "i":9, "í":9,
        "J":10, "j":10,
        "K":11, "k":11,
        "L":12, "l":12,
        "M":13, "m":13,
        "N":14, "n":14,
        "Ñ":15, "ñ":15,
        "O":16, "Ó":16, "o":16, "ó":6,
        "P":17, "p":17,
        "Q":18, "q":18,
        "R":19, "r":19,
        "S":20, "s":20,
        "T":21, "t":21,
        "U":22, "Ú":22, "u":22, "ú":22, "ü":22,
        "V":23, "v":23,
        "W":24, "w":24,
        "X":25, "x":25,
        "Y":26, "y":26,
        "Z":27, "z":27,
        }
    
    codigos = []
    for letra in cadena:
        codigos.append(alfabeto[letra])
    return codigos

nombres.sort(key= ord_alf)
print(nombres)

# para que el orden empiece por M (m = 13):
nombres.sort(key= lambda p: ord_alf(p) if ord_alf(p)[0] > 12 else \
             [100] + ord_alf(p)) # ponemos 100 porque sabemos que solo llega hasta 27...
'''
tb podríamos haber puesto :
nombres.sort(key= lambda p: [-1] + ord_alf(p) if ord_alf(p)[0] > 12 else ord_alf(p))
'''

print(nombres)