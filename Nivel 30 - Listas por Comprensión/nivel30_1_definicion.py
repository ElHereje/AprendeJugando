

# numeros = [1, 2, 3, 4,5 ]

'''
podemos crear una lista añadiendo valores a esa lista:
numeros = []
for n in range(1, 6):
    numeros.append(n)
print(numeros)
'''
'''si lo hacemos por comprensión:

[expresion      for elemento        in iterable]
    n               for n            in cadena
   n**2             for n            in range(1, 10)
 (n*2)%3            for n            in lista
'''
numeros =[n for n in range(1, 6)]
print(numeros)

# dobles del 1 al 10
dobles = [n*2 for n in range(1,11)]
print(dobles)


'''
ejercicio ---> crear una lista, por comprensión, que contenga 5 cadenas 
de caracteres, con uno, dos, tres cuatro y cinco asteriscos.
'''