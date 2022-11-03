"""
giran en torno a una máxima --> intentar que las funciones sean lo más
simples posible (una sola tarea)  para así ser lo mas reutilizable y
mantener sencillez y claridad en el código
"""

# función que sume y muetre el resultado
def sumar(sum1, sum2):
    print(sum1  + sum2)

# esta función es correcta, pero realiza 2 tareas:
# sumar y mostrar por pantalla. Por otra parte, el resultado
# no se almacena...

#sería mejor
def sum_correcto(sum1, sum2):
    return sum1 + sum2

# ahora solo hace 1 tarea, y podemos guardar el dato
suma = sum_correcto(2, 5)
print(suma)

# .. y operar con ella:
suma_total = sum_correcto(2, 2)  + sum_correcto(3, 3)
print(suma_total)


# esta vez, en la funcion queremos incluir inputs
def suma3():
    sumando1 = input("Introduce el primer nº: ")
    sumando2 = input("Introduce el segundo nº: ")
    print(sumando1 + sumando2)

# esta función hace 3 cosas.. vamos a intentar mejorarla, sustituyendo
# el print y pidiendo los datos fuera

def suma4(sumando1, sumando2):
    return sumando1 + sumando2

n1 = int(input("Introduce el primer nº: "))
n2 = int(input("Introduce el segundo nº: "))

suma_fnal = suma4(n1, n2)
print(suma_fnal)

