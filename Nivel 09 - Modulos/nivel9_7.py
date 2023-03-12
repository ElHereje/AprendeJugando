# Lanzando una moneda.

"""
Programa que simule 100 tiradas de una moneda y
comprueba cuantas veces sale cada resultado
"""

import random

veces_cara = 0
veces_cruz = 0
for i in range(100):
    tirada = random.choice(["cara", "cruz"])
    if tirada == "cara":
        veces_cara += 1
    elif tirada == "cruz":
        veces_cruz += 1
print(f"Han salido {veces_cara} caras y {veces_cruz} cruces...")
