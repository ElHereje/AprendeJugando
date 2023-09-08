
tarjetas = [5, 7, 3, 1, 8, 4, 9, 2, 6]

longitud = len(tarjetas)
for i in range(longitud - 1):
    print(tarjetas)
    menor = i
    print("El indice actuacl es", menor)
    for j in range(i+1, longitud):
        if tarjetas[j] < tarjetas[menor]:
            menor = j
            print("Recorriendo lista. Es menor el indice ", menor)
    temporal = tarjetas[menor]
    tarjetas[menor] = tarjetas[i]
    tarjetas[i] = temporal
    print("Cambiamos el elemento ", tarjetas[menor], "por ", tarjetas[i])