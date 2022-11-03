"""
hasta ahora hemos visto funciones que le damos un nº deterninado
de argumentos:
"""
def nota_media(n1, n2, n3, n4):
    return (n1 + n2 + n3 + n4) / 4
print(nota_media(6, 8, 7, 9))   # --> 7.5


"""
Pero esto solo vale para 4 NOTAS, ni mas ni menos.
¿Como hacemos para un nº indefinido de argumentos?
"""
# podemos hacer un desempaquetado de una lista:
notas = [6, 8, 7, 9]
print(nota_media(*notas))  # --> 7.5


"""
Una posible solución sería tener las notas en una lista
"""
def nota_media2(notas):
    # suma = 0
    # for i in notas:
    #     suma += i
    # media = suma / len(notas)
    # return media
    return sum(notas)/len(notas)
print(nota_media2(notas))   # --> 7.5


"""
En el caso de que no estuvieran en una lista, sino valores independientes,
haríamos el proceso contrario (empaquetado), pero en la función:
"""
nota1 = 6
nota2 = 8
nota3 = 7
nota4 = 9

def nota_media3(*notas):
    return sum(notas)/ len(notas)

print(nota_media3(nota1, nota2, nota3, nota4))


