"""
En una lotería hay un bombo que tiene 10 bolas, con los números del 1 al 10.
En un sorteo se sacan 5 bolas, sin que se introduzcan de nuevo.
Haz un programa que muestre todas las posibles apuestas, es decir,
todas las combinaciones posibles que se pueden dar en esa lotería.
Incluye un contador para comprobar el número de combinaciones que se dan.

Serían Combinaciones sin repetición de 10 elementos tomados de 5 en 5.
No importa el orden

10! / 5!*(10-5)! = 10*9*8*7*6 / 5*4*3*2*1 = 30240/120 = 252 posibilidades

"""

combinaciones = []
contador = 0

# 5 bucles para cada uno de los elementos de la combinación...
for i in range(1, 11):
    for j in range(1, 11):
        for k in range(1, 11):
            for m in range(1, 11):
                for n in range(1, 11):
                    # nos quedamos solo con las combinaciones que no se repiten
                    if (i != j and i != k and i != m and i != n and
                            j != k and j != m and j != n and
                            k != m and k != n and m != n):
                        comb = [i, j, k, m, n]
                        # ordenamos y eliminamos las repeticiones
                        comb.sort()
                        if comb not in combinaciones:
                            combinaciones.append(comb)
                            contador += 1
                            # podemos verlas como prueba:
                            print(f"{contador:3} : {comb}")
print(f"{contador} combinaciones posibles")


