# MEJORADO (USANDO EL OPERADOR IS)

n1 = int(input("Dime un número: "))
n2 = int(input("Dime un número: "))
n3 = int(input("Dime un número: "))
n4 = int(input("Dime un número: "))
n5 = int(input("Dime un número: "))
n6 = int(input("Dime un número: "))
n7 = int(input("Dime un número: "))

mayor = None

if mayor is None:
    mayor = n1
if n2 > mayor:
    mayor = n2
if n3 > mayor:
    mayor = n3
if n4 > mayor:
    mayor = n4
if n5 > mayor:
    mayor = n5
if n6 > mayor:
    mayor = n6
if n7 > mayor:
    mayor = n7


print(f"El número mayor es {mayor}")


