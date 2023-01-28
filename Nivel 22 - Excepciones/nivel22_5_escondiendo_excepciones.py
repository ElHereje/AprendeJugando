'''
Programa que calcula raices cuadradas - USAR EXCEPCIONES

no es posible raiz de un nº negativo

import math

numero = float(input("Introduce un número: "))
resultado = math.sqrt(numero)
print(f"Raiz cuadrada: {resultado}")


SI NO PONEMOS EL NOMBRE DEL ERROR, CAPTURA CUALQUIER ERROR Y NOS 
INFORMA DEL MISMO.


'''

import math

while True:
    try:
        numero = float(input("Introduce un número: "))
        resultado = math.sqrt(numero)
    except:
        print("Introduce nº correcto...")
    else:
        print(f"Raiz cuadrada: {resultado}")
        break