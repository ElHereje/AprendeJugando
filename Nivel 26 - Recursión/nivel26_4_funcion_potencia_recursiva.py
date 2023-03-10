'''
Crear una función recursiva para calcular la potencia de un nº.
En esta ocasión, el caso base sería la potencia de 0

2^4 = 2*2^3 = 2*2*2^2 = 2*2*2*2^0 = 2*2*2*2*1

potencia(2,4):
    2 * potencia(2,3):
        2 * potencia(2,2):
            2 * potencia(2,1):
                2 * potencia(2,0):
                    1
                2 * 1
            2 * 2 * 1
        2 * 2 * 2 * 1
    2 * 2 * 2 * 2 * 1

def potencia(base, exp):
    if exp == 0:
        resultado =  1
        print("caso base", resultado)
    else:
        print("No hemos llegado", exp)
        resultado =  base * (potencia(base, exp-1))
        print("Saliendo", resultado)
    return resultado
    
print(potencia(5,5))

'''
# la misma función optimizada:

def potencia(base, exp):
    if exp == 0:
        return 1
    else:
        return base * (potencia(base, exp-1))
    
print(potencia(5,8))