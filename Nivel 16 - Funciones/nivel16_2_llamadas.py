"""
Define una función que tome como parámetro un número y
devuelva el triple del doble de ese número.

Llama a la función y pásale como argumento un número que pidas
al usuario. Muestra el resultado por pantalla.
"""

def triple_del_doble(n):
    return 3*(2*n)

incognita = float(input("Introduce el número a calcular : "))
print(triple_del_doble(incognita))