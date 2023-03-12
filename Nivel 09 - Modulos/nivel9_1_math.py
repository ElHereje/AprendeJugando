# EL MÓDULO MATH

"""import math
print(math.sqrt(9))  # --> 3"""

"""
Programa que calcule el perímetro  y el área de
una circunferencia
P=2*pi*r
área = pi*r*r
"""
import math

radio = float(input("Dime el radio de la circunferencia: "))
perimetro = 2 * math.pi * radio
area = math.pi * (radio ** 2)

print(f"El perímetro vale {perimetro}, y su área {area}.")


