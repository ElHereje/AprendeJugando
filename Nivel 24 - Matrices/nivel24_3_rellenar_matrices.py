'''
Programa que crea una matriz con los datos que introduces:
Filas, columnsa, y valores para cada elemento.
'''

filas = int(input("Introduce nº de filas: "))
columnas = int(input("Introduce nº de columnas: "))

matriz = []
 
# creamos la matriz y la vamos rellenando
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        valor = float(input(f"Valor para Fila {i+1}, Columna {j+1} : "))
        matriz[i].append(valor)    
        
for fila in matriz:
    print("[", end=" ")
    for elemento in fila:
        print(f"{elemento:8.2f}", end=" ")
    print("]")
    
print()