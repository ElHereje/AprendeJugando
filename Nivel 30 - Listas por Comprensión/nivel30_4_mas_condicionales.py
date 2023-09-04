''' 
ejercicio --> crea una lista con las palabras de mas de 7 letras

utiles = ["mesa", "interruptor", "silla", "microscopio", "cubo"]


utiles = ["mesa", "interruptor", "silla", "microscopio", "cubo"]
lista = [palabra for palabra in utiles if len(palabra)>7]
print(lista) '''


# lista con el nº siguente a los nºs del 1 al 30
# que sean múltiplos de 7 o 11:

'''lista = [n+1 for n in range(1, 31) if n % 7 == 0 or n % 11 == 0]
print(lista)'''


# Tb podemos incluir un bloque "else":
# lista con los pares y 0 si es impar (el else se coloca antes de la condición)

datos = [2, 3, 5, 8, 9, 10, 12, 15]
pares = [n if n%2 == 0 else 0 for n in datos]
print(pares)


'''
EJERCICIO

Crear una lista co el tipo de dato de cada uno
de los elementos de la lista datos:
- si son cadenas de caracteres: "cadena"
- si son enteros o float: "numérico"

datos = [7, "h", 2.5, "m", 8.2, 24, "p"]

'''