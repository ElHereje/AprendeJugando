'''
mcd por algoritmo de EUCLIDES

si tenemos 2 nº enteros, en el que el mayor es distinto de 0,
por el algoritmo de la división tenemos que :
        a = b * q + r
entonces:
        mcd(a,b) = mcd(b,r)

ejemplo 12 y 8  --> 12 = 8 * 1 + 4
        mcd(12, 8) = mcd(8, 4)

explicación
 ---------------- 16
 ----------       10
 ------            6
 ----              4
 --                2

 16%10=6
 10%6=4
 6%4=2
 4%2=0    -->  mcd = 2

mcd(16, 10) = mcd(10, 6) = mcd(6, 4) = mcd(4, 2) = mcd(2, 0) = 2
'''

# def mcd_euclides(n1, n2):
#     while True:
#         resto = n1 % n2
#         if resto == 0:
#             return n2
#         else:  # cambiamos los valores..
#             n1 = n2
#             n2 = resto
#
# a = int(input("Introduce nº1: "))
# b = int(input("Introduce nº2: "))
# print(f"El mcd de {a} y {b} es {mcd_euclides(a, b)}")

# ahora solo queda optimizarlo..

def mcd_euclides(n1, n2):
    while n1 % n2 != 0:
        n1, n2 = n2, n1 % n2
    return n2

a = int(input("Introduce nº1: "))
b = int(input("Introduce nº2: "))
print(f"El mcd de {a} y {b} es {mcd_euclides(a, b)}")