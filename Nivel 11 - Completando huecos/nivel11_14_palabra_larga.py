"""
Encontrar la palabra más larga, y si hay varias con igual
longitud, será la primera de todas
"""

lista_palabras = ["mesa", "armario", "silla", "lámpara", "cuadro"]
long_mayor = 0
mas_larga = None

for palabras in lista_palabras:
    if len(palabras) > long_mayor:
        long_mayor = len(palabras)
        mas_larga = palabras

print(f"La palabra más larga es {mas_larga}")
