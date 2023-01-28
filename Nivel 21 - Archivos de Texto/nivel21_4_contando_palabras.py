"""
Mostrar qué 5 palabras de más de 12 letras aparecen más veces
en el Quijote, y cuantas veces aparece cada una.
"""
archivo = open("quijote.txt", "r", encoding="utf-8")
texto = archivo.read()
archivo.close()

# separamos el texto en palabras
lista = texto.split()

# limpiamos la lista
palabras = {}  # diccionario vacío
for elemento in lista:
    palabra = elemento.strip(".").strip(",").strip(":")
    # aplicamos condiciones {palabra:veces}
    if len(palabra) > 12:
        palabras.setdefault(palabra, 0)  # si no está, la incluye
        palabras[palabra] += 1  # aumenta en 1 el valor de la clave palabra

# ya tenemos en el diccionario las palabras mayores de 12 y el nº de veces
# ahora solo hay que mostrarlas
for i in range(5):
    numero_mayor = 0
    for palabra in palabras:
        if palabras[palabra] > numero_mayor:
            numero_mayor = palabras[palabra]
            palabra_mayor = palabra
    print(palabra_mayor, ":", numero_mayor)
    # excluimos esa palabra
    del palabras[palabra_mayor]

