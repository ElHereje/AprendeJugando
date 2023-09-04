'''
ejercicio --> crear una lista con las iniciales de las palabras de la lista
palabras = ["casa", "mesa", "silla", "puerta", "ventana"]


palabras = ["casa", "mesa", "silla", "puerta", "ventana"]
iniciales  = [letra[0] for letra in palabras]
print (iniciales)

'''

# para añadir elementos con un condicional: 

datos = [14, 18, 21, 29, 36, 41, 58, 63, 74]

pares = [n for n in datos if n%2==0]
print(pares)
mayores_de_30 = [n for n in datos if n > 30]
print(mayores_de_30)
pares_mayores_de_30 = [n for n in datos if n%2==0 and n>30]
print(pares_mayores_de_30)


''' 
ejercicio --> crea una lista con las palabras de mas de 7 letras

utiles = ["mesa", "interruptor", "silla", "microscopio", "cubo"]
'''
