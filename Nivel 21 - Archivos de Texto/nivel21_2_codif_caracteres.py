# La codificación es importante si vamos a usar doc. externos
"""
Para poder representar los caracteres en un ordenador se necesita
un sistema de codificación y ello supone reservar un espacio de  memoria
para cada uno de ellos

Hasta hace poco este espacio era de:
        1 byte = 8 bits = 00000000

Las combinaciones posibles de 8 bits con 1 y 0 son 256

Con lo cual si se usa 1 byte para guardar la información necesaria para
procesar un carácter podemos tener 256 caracteres guardados en un
sistema de 8 bits.

El formato ASCII al ppio usaba 7 bits, 128 caracteres. Posteriormente
pasó a usar 8 bits.

El formato ANSI usa 1 byte y es el usado en windows. No es standard.
En europa se usa el cp1252, pero no contiene caracteres de otros idiomas

UNICODE es un juego de caracteres establecido internacionalmente que contiene
los caracteres posibles necesarios para ser representados en un ordenador.
No es un sistema de codificación en sí, sino que se implementa en los ordenadores
a través del sistema UTF-8, UTF-16 o UTF-32

"""
archivo_UTF = open("saludo_UTF-8.txt")
archivo_ANSI = open("saludo_ANSI.txt")
texto1 = archivo_UTF.read()
texto2 = archivo_ANSI.read()
archivo_ANSI.close()
archivo_UTF.close()
print("UTF")
print("---")
print(texto1)
print()
print("ANSI")
print("----")
print(texto2)

archivo_convertido = open("saludo_UTF-8.txt", encoding="UTF-8")
texto3 = archivo_convertido.read()
archivo_convertido.close()
print(texto3)