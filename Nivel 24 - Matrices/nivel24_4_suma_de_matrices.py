'''
Definir una función que dadas 2 matrices calcules su suma.
- Sólo se pueden sumar matrices del mismo orden.
- El resultado es otra matriz del mismo orden que las sumadas.
'''

a = [[21, 18, 35, 40],
     [19, 11, 21, 14],
     [12, 15, 20, 30]]

b = [[11, 7, 21, 32],
     [9, 15, 24, 10],
     [23, 8, 12, 22]]


def sumar_matrices(m1, m2):
    # comprobamos que sean del mismo orden
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):  #  filas and columnas 
        m3 = []
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m1[0])):
                m3[i].append(m1[i][j] + m2[i][j])
        return m3
    else:
        return None
    
    
c = sumar_matrices(a, b)
if c == None:
    print("No se pueden sumar...")
else:
    for fila in c:
        print("[", end=" ")
        for elemento in fila:
            print(f"{elemento:8.2f}", end=" ")
        print("]")
            