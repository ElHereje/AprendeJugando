'''
Rotar una matriz 90º en el sentido del reloj.
 

flecha = [
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0]
    ]


rotada[i][j] = original[len(original) - 1 - j][i]

'''

# matriz = [
#     [11, 12, 13, 14, 15],
#     [21, 22, 23, 24, 25],
#     [31, 32, 33, 34, 35],
#     [41, 42, 43, 44, 45]
# ]

flecha = [
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0]
    ]

def rotar_matriz(m):
    rotada = []
    for i in range(len(m[0])):
        rotada.append([])
        for j in range(len(m)):
            rotada[i].append(m[len(m) - 1 - j][i])
    return rotada

print("------------------")

for fila in flecha:
    for e in fila:
        print(e, end=" ")
    print()
        
print("------------------")


rotada_2 = rotar_matriz(flecha)

for fila in rotada_2:
    for e in fila:
        print(e, end=" ")
    print()
    
print("------------------")

rotada_3 = rotar_matriz(rotada_2)

for fila in rotada_3:
    for e in fila:
        print(e, end=" ")
    print()
        
print("------------------")

rotada_4 = rotar_matriz(rotada_3)

for fila in rotada_4:
    for e in fila:
        print(e, end=" ")
    print()

