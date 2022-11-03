"""
programa que pide 7 números e indica cual es el mayor.
"""
# lo vamos a realizar de 2 maneras.

# BÁSICA

n1 = int(input("Dime un número: "))
n2 = int(input("Dime un número: "))
n3 = int(input("Dime un número: "))
n4 = int(input("Dime un número: "))
n5 = int(input("Dime un número: "))
n6 = int(input("Dime un número: "))
n7 = int(input("Dime un número: "))

if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5 and n1 > n6 and n1 > n7:
    mayor = n1
elif n2 > n3 and n2 > n4 and n2 > n5 and n2 > n6 and n2 > n7:
    mayor = n2
elif n3 > n4 and n3 > n5 and n3 > n6 and n3 > n7:
    mayor = n3
elif n4 > n5 and n4 > n6 and n4 > n7:
    mayor = n4
elif n5 > n6 and n4 > n7:
    mayor = n5
elif n6 > n7:
    mayor = n6
else:
    mayor = n7
print(f"El número mayor es {mayor}")

