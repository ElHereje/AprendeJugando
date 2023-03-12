"""
También podíamos haber importado solo la función necesaria
Así no hay que especificar el módulo del que procede
al usarlo.
"""

from math import pi

radio = float(input("Dime el radio de la circunferencia: "))
perimetro = 2 * pi * radio
area = pi * (radio ** 2)

print(f"El perímetro vale {perimetro}, y su área {area}.")
