'''
Orden de complejidad:

O(1) - Constante
O(n) - Lineal
O(n exp 2) - Cuadrática
O(n exp a)  - Polinomial
O(log n) - Logarítmica
O(2 exp n) - Exponencial

Es importante la "tasa de crecimiento", que evalua el rendimiento
de una función al aumentar el numero de datos


Notación asintótica

O grande - El peor de los casos
Ω grande - El mejor d elos casos
θ grande - Caso promedio


con O grande, vamos a saber el tiempo de ejecución en el peor de los casos

'''
    
    
# ejemplo

# Es una medida estimada
# Se ignoran las constantes
# Solo se toma el término mas complejo

def suma_lineal(n):
    suma = 0
    for i in range(cantidad + 1): # (1, n+1)
        suma = suma + i
    return suma
# op. --> 1 + n * 2 = 1 + 2n --> n
# O(n)


def suma_constante(n):
    return (n/2) * (n+1)
# operaciones --> 1 + 1 +1 = 3 
# O(1)
    
    
    
# ejemplo

lista_datos = [14, 26, 39, 25, 11, 18, 42, 31, 17, 23]
buscado = 31

cantidades = [12, 23, 41, 37, 28, 54, 35, 46, 52, 19, 27]
numero = 74

# def busqueda_lineal(lista, buscado):
#     for elemento in lista:
#         if elemento == buscado:
#             return True
#     return False

# se podria optimizar
def busqueda_lineal(lista, buscado):
    if buscado in lista:
        return True
    return False

def sum_tres(lista, valor):
    '''comprueba si la sma de 3 numeros de una lista
    tienen un resultado dado'''
    
    # complejidad polinomial O(n^a)
    trios = []
    for i in lista:
        for j in lista:
            for k in lista:
                if i+j+k == valor:
                    trios.append([i,j,k])
                    print(i,j,k)
    return trios


if busqueda_lineal(lista_datos, buscado):
    print("Dato encontrado")
else:
    print("Dato no encontrado")
    

print(sum_tres(cantidades, numero))
    


