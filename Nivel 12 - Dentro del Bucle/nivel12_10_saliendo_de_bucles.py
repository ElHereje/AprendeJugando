# Una manera de mejorar lo anterior es crear un sistema para
# salir del bucle cuando encuentra la clave.
# También se puede mejorar considerando que la clave puede
# tener menos de 5 caracteres (entre 1 y 5 caracteres)

import time

# el que pueda tener menos de 5 caracteres se consigue simplemente
# poniendo un espacio al principio de la cadena
alfabeto = " aAbBcCdDeEfFgGhHiIjJkKlLmMnNñÑoOpPqQrRsStTuUvVwWxXyYzZ1234567890"
inicio = time.time()
intento = None
clave = input("Dime una clave de 5 letras (MAY Y MIN): ")

for l1 in alfabeto:
    if intento != clave:
        for l2 in alfabeto:
            if intento != clave:
                for l3 in alfabeto:
                    if intento != clave:
                        for l4 in alfabeto:
                            if intento != clave:
                                for l5 in alfabeto:
                                    temporal = l1 + l2 + l3 + l4 + l5
                                    # eliminamos los espacios delante y detrás
                                    intento = temporal.strip()
                                    if intento == clave:
                                        print(f"Clave encontrada: {clave}")
                                        break
                            else:
                                break
                    else:
                        break
            else:
                break
    else:
        break

final = time.time()
print(f"Tiempo consumido: {final-inicio:5.2f} segundos")

