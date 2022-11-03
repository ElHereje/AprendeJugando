#  EL TIPO range

# es un tipo de datos "secuencia".
# Almacena y crea secuencia de nº enteros, pero como INTERVALO

print(range(10))  # --> range(0, 10)
print(10 in range(10))  # --> False

# estructura --> range(comienzo, final sin incluir, salto)

'''
Programa que pida un nº entero que esté en el intervalo del 18 al 25
y que siga pidiendo nº mientras te mantenga ese intervalo

Utiliza el tipo range 
'''

prueba = True
while prueba:
    dato = int(input("Introduce un nº del intervalo 18-25: "))
    if dato in range(18, 25):
        print(f"Correcto, {dato} está dentro del rango")
    else:
        prueba = False
        print(f"Nº {dato} fuera del rango.")
        print("Fin del programa")

