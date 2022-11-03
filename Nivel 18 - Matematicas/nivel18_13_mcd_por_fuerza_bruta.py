
def mcd_brute_force(n1, n2):
    # 1º calculamos el menor de los nº
    if n1 < n2:
        i = n1
    else:
        i = n2

    # ahora vamos probando desde el menor hacia abajo:
    while not (n1 % i == 0 and n2 % i == 0):
        i -= 1
    else:  # --> cuando se cumpla..
        return i

a = int(input("Introduce nº1: "))
b = int(input("Introduce nº2: "))
print(f"El mcd de {a} y {b} es {mcd_brute_force(a, b)}")

# este algoritmo es mas eficiente, pero la necesitamos mas rápida.
# vamos a ver el algoritmo de EUCLUDES