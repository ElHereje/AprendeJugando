# MÓDULO TIME

import time

#print(time.time())
# ESTO DEVUELVE EL TIEMPO DESDE EL 1 DE ENERO DE 1970

# Programa donde jugamos a que pase el tiempo:

inicio = time.time()
while True:
    print("Estamos jugando...")
    final = time.time()
    if final - inicio >= 5: # transcurso de 5 seg.
        break
print("Fin del juego")
print(f"Tiempo transcurrido : {final - inicio} seg.")