'''
vamos a definir una función factorial recursiva.
Esta ya la hemos hecho con una función iterativa:

def fact(n):
    resultado = 1
    for i in range(n)
        resultado *= n-i
    return resultado
print(fact(5))

para hacerlo de manera recursiva:
5! = 5*4! = 5*4*3! = 5*4*3*2! = 5*4*3*2*1! = 5*4*3*2*1*1

fact(5) = 5 * fact(4)
fact(4) = 4 * fact(3)
fact(3) = 3 * fact(2)
fact(2) = 2 * fact(1)
fact(1) = 1 * fact(0)
fact(0) = 1 ---------------> Caso Base, cuando n = 0 --> Se comienzan a realizar los cálculos
fact(1) = 1 * 1
fact(2) = 2 * 1 * 1
fact(3) = 3 * 2 * 1 * 1
fact(4) = 4 * 3 * 2 * 1 * 1
fact(5) = 5 * 4 * 3 * 2 * 1 * 1

'''
# Para hacerlo de forma recursiva:
def fact(n):
    if n == 0:
        resultado = 1
        print(f"Hemos llegado al caso BASE. n = {n}")
    else:
        print(f"No hemos llegado al caso Base. n = {n}")
        resultado = n * fact(n - 1)
        print(f"Estamos saliendo de la recursión. n = {n} , resultado = {resultado}")
    return resultado

print(fact(5))
