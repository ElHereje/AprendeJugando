'''
Definir una función que dadas dos matrices calcule su multiplicación.

- Columnas de la 1ª matriz han de ser iguales a filas de la 2º.
- Resultado será una matriz de orden de filas de la 1ª por columnas de 2ª 

a = [[a11, a12],
     [a21, a22]

b = [[b11, b12]
     [b21, b22]]
     
a * b = [[a11*b11 + a12*b21    ,   a11*b12 + a12*b22]
         [a21*b11 + a22*b21    ,   a21*b12 + a22*b22]]

'''

a = [[1, 2, 3],
     [4, 5, 6]]

b = [[1, 2],
     [3, 4],
     [5, 6]]


def mult_matrices(m1, m2):
    # 1º verificamos requisitos
    if len(m1[0]) == len(m2):
        m3 = []
        # creamos la matriz cero
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m2[0])):
                m3[i].append(0)
                
        # rellenamos los valores
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m1[0])):
                    m3 [i][j] += m1[i][k] * m2[k][j]
        return m3
    else:
        return None

c = mult_matrices(a, b)
if c == None:
    print("No se pueden multiplicar.")
else:
    for fila in c:
        print("[", end=" ")
        for elemento in fila:
            print(f"{elemento:8.2f}", end=" ")
        print("]")
                
        