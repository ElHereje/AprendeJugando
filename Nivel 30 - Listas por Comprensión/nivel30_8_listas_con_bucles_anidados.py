# lista con los pares de numeros posibles con los nºs del 1 al 5:
# (variaciones con repeticion con los elelemntos del 1 al 5 tomados de 2 en 2)

# 1º sin listas por comprension
pares = []
for i in range(1, 6):
    for j in range(1, 6):
        pares.append((i, j))

print(pares)

# 2º con listas por comprension
pares_2 = [(i,j) for i in range(1,6) for j in range(1,6)]
print(pares_2)

# -----------------------------------------------------------------------------------

# combinaciones entre listas (producto cartesiano)
formas = ["Cuadrado", "Triángulo", "Círculo"]
colores = ["Rojo", "Verde", "Azul", "Blanco"]

pares = [(f, c) for f in formas for c in colores]
for elementos in pares:
    print(elementos)

# -------------------------------------------------------------------------------------

# sumar elemntos de cada lista siempre que el resultado sea mayor que 10

datos_1 = [2, 3, 5]
datos_2 = [2, 4, 6]
datos_3 = [1, 3, 4]

sumar_mayores_10 = [i+j+k
                    for i in datos_1
                    for j in datos_2
                    for k in datos_3
                    if i+j+k > 10] 
print(sumar_mayores_10)


# -----------------------------------------------------------------------------------------


'''
RETO --> Lisrta con los pares de elementos de cantidades y aumentos, tales que
si sumamos una cantidad par mas un aumento impar o una cantidad impar mas un
aumento par tiene que dar 11

cantidades = [1, 4, 6, 7, 8]
aumentos = [2, 3, 4, 5, 6]

'''