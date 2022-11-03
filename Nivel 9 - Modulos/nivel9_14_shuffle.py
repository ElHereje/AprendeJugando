# SHUFFLE lo que hace es barajar las opciones dadas:

import random

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(lista)
random.shuffle(lista)
print(lista)


# SAMPLE coge una muestra de la lista entre datos indicados

print(random.sample(lista, 3))