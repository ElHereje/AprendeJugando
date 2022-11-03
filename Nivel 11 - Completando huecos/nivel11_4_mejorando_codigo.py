# MEJORADO (UN SOLO INPUT)


mayor = None

for i in range(7):
    n = int(input("Dime un número: "))
    if mayor is None or n > mayor:
        mayor = n

print(f"El número mayor es {mayor}")