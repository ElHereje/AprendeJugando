'''
Traspuesta de una matriz:

Trasponer (cambiar, trasladar) los elementos de las filas
a las columnas, y viceversa.

m = [[1, 2, 3],
     [4, 5, 6]]
     
t = [[1, 4],
     [2, 5],
     [3, 6]]

'''

matriz = [[1, 2, 3],
          [4, 5, 6]]

def trasponer(m):
    # comenzamos por una lista vacía:
    t = []
    for i in range(len(m[0])):
        t.append([])
        # cambiamos el indice de las filas por el de las columnas
        for j in range(len(m)):
            t[i].append(m[j][i])
    return t

traspuesta = trasponer(matriz)

# mostramos la matriz original para verificar
print()
for linea in matriz:
    for elemento in linea:
        print(elemento, end=" ")
    print()
    
print("------------------")
print()

for linea in traspuesta:
    for elemento in linea:
        print(elemento, end=" ")
    print()
print()