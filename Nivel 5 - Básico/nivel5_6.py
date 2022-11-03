# dados 3 números indicar el mayor

n1 = int(input("Introduce número 1: "))
n2 = int(input("Introduce número 2: "))
n3 = int(input("Introduce número 3: "))
print(f"Los números son: {n1}, {n2} y {n3}")
if n1 > n2:
    if n1 > n3:
        print(f"El mayor es {n1}")
else:
    if n2 > n3:
        print(f"El mayor es {n2}")
    else:
        print(f"El mayor {n3}")