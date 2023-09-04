'''
ejercicio ---> crear una lista, por comprensión, que contenga 5 cadenas 
de caracteres, con uno, dos, tres cuatro y cinco asteriscos.
'''

cadenas = ["*" * n for n in range(1, 6)]
print (cadenas)


'''
podemos usar otras listas como elementos:
'''

numeros = [1, 2, 3, 4]
cuadrados = [n**2 for n in numeros]
print (cuadrados)

'''tambien podemos tener como iterable una cadena de caracteres: '''

cadena = "artefacto"
letras = [letra for letra in cadena]
print (letras)


'''
ejercicio --> crear una lista con las iniciales de las palabras de la lista
palabras = ["casa", "mesa", "silla", "puerta", "ventana"]

'''