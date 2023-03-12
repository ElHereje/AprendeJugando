# FÓRMULAS MATEMÁTICAS

"""
Calcula la hipotenusa de un triángulo rectángulo con
el teorema de Pitágoras.

los lados del ángulo recto son 3 y 4
"""

import math

a = float(input("Dime uno de los catetos: "))
b = float(input("Dime el otro cateto. "))

c = math.sqrt((a**2) + (b**2))
print(f"La hipotenusa vale {c}")


# ********************************

''' 
Calcula el perímetro de una elipse
per = 2 * PI * RAIZ((r*r) + (s*s) / 2
'''

r = float(input("Dime un semieje: "))
s = float(input("Dime el otro: "))
p = 2 * math.pi * math.sqrt((r**2 + s**2)/2)
print(f"El perímetro de la elipse vale {p}")
