'''
Son funciones que devuelven valores lógicos.

bool
----
enteros --> todos true escepto el 0
cadenas --> todos true escepto una cadena vacía
None --> False
True --> True
False --> False
Listas --> si están vacías, siempre es false

any
---
estructura --> any(iterable, /) si el valor de algún iterable es True, la función será True
                                si todos fueran false, la función será False
            any([0,0,0]) --> False
            any([0,0,1]) --> True
            any([]) --> false


all
----
Todos los elementos deben tener valor True, de lo contrario sería false

otros
-----
isalpha() --> todo caracteres
isdigit() --> todo números
isalnum() --> todosalfanumérico
islower(), isupper(),.....



RETO --> define una función que valide contraseñas.
Ha de comprobar:
- Entre 6 y 12 caracteres
- Al menos una letra
- Al menos un dígito
- Al menos una mayusc.
- Al menos una minusc.
- Al menos un carcater especial

'''