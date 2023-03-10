'''En la definición de una función, se puede incluir una llamada
a sí misma. Siempre debe de haber un caso base (condición para salir de
la recursión), en el que la función deje de llamarse a sí misma 
(si no entraríamos en bucles infinitos)

Ete proceso es similar a la iteración (while)

'''

# def mirarse_al_espejo():
#     print("Me miro al espejo y veo que...")
#     mirarse_al_espejo()

# mirarse_al_espejo()

# esto sería agual a...
# while True:
#     print("Me miro al espejo y veo que...")

# un ejemplo util sería por ejemplo una cuenta atras:
# def cuenta_atras(n):
#     while n >= 0:
#         print(n)
#         n -= 1
# cuenta_atras(10)

# este ejemplo se puede hacer con recursión:
# (el caso base es llegar a cero)

def cuenta_atras(n):
    
    if n < 0:
        print("Fin")
    else:
        print(n)
        n -= 1
        cuenta_atras(n)

cuenta_atras(10)