# programa que sume los nº pares del 1 al 10

suma = 0
n = 0
while n <= 20:
    if n % 2 == 0:
        suma += n
    n += 1
print(suma)


# ********************************


# programa que pida intervalo de números y que sume
# todos los múltiplos de 3


inicial = int(input("Introduce el primer número: "))
final = int(input("Introduce el último número: "))

sum = 0
while inicial <= final:
    if inicial % 3 == 0:
        sum += inicial
    inicial += 1
print(sum)