"""
Programa que informa del nº de datos que se han recogido.
Pide el nº de datos que se mantienen y borra el resto.
Usar la sentencia "del".
"""

datos = [1.12, 2.18, 1.45, 2.21, 3.07, 2.32, 3.41, 1.39]

print(datos)
print(f"Se han recogido {len(datos)} datos...")
n = int(input("Introduce el nº de datos a mantener (1 - 8) : "))
while n > len(datos):
    print(" te has excedido en el nº de valores.... ")
    n = int(input("Introduce el nº de datos a mantener (1 - 8) : "))
else:
    del datos[n: len(datos)]

for i in range(len(datos)):
    print(f"- {datos[i]}")