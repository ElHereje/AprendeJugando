"""Programa que pida 5 números y los va sumando.
Al final te muestra el resultado (usar FOR)"""


'''
suma = 0
for i in range(5):
    num = int(input(f"Introduce número {i+1}: "))
    suma += num
print(f"la suma de los números introducidos es {suma}")
'''


'''
Programa que va pidiendo números y los va sumando 
hasta que alcanza 100 o más. Entonces para y muestra el 
resultado. (usar FOR)  --> NO SE PUEDE
'''

suma = 0
while suma <= 100:
    num = int(input(f"Introduce número: "))
    suma += num
print(f"la suma de los números introducidos es {suma}")
