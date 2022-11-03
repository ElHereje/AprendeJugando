# STRIP Y SPLIT

respuesta = " s "
print(respuesta.strip())  # --> elimina los espacios o el caracter que pongamos
res2 = "hola,"
print(res2.strip(","))
res3 = ".hola."
print(res3.strip("."))

# *******************************

# split separa según el criterio que indiquemos.
# si no se pone nada, entiende que son espacios.

frase = "Hace un día estupendo. El sol brilla."
print(frase.split())  # --> ['Hace', 'un', 'día', 'estupendo.', 'El', 'sol', 'brilla.']

'''
Programa que recoge todas las palabras de un texto
y las devuelve sin espacios, comas ni puntos
'''

cadena = '''Estaba allí. Era un pájaro, en la ventana. Pero
entonces, de repente, se echó a volar.'''

palabras = cadena.split()
print(palabras)

for palabra in palabras:
    sin_comas = palabra.strip(",")
    sin_puntos = sin_comas.strip(".")
print(n)
