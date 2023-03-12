# OPERADOR 'in'

# programa que te dice las vocales que tiene una palabra

'''vocales = "aeiouáéíóú"

palabra = input("Introduce una palabra: ")
contador = 0
indice = 0

while indice < len(palabra):
    if palabra[indice] in vocales:
        contador += 1
    indice += 1
print(f"La palabra {palabra} tiene {contador} vocales")'''

# programa que dice las vocales y consonantes que tiene una palabra

vocales = "aeiouáéíóú"
consonantes = "bcdfghjklmnñpqrstvwxyz"
palabra = input("Introduce una palabra: ")
contador_v = 0
contador_c = 0
indice = 0

while indice < len(palabra):
    if palabra[indice] in vocales:
        contador_v += 1
    elif palabra[indice] in consonantes:
        contador_c += 1
    indice += 1
print(f"La palabra {palabra} tiene {contador_v} vocales y {contador_c} consonantes")


