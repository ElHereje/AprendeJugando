'''

vamos a ver como capturar las excepciones. vamos a usar un ejemplo
de un ejercicio anterior para ver si un usr es mayor de edads

'''
# try:
#     numero = int(input("Dime tu edad: "))
#     if numero >= 18:
#         print("Eres mayor de edad.")
#     else:
#         print("No eres mayor de edad.")
# except ValueError:  # por si no se ponen enteros:
#     print("No has introducido un nº entero...")
    
# esto se puede optimizar con otro bloque --> else:

try:
    numero = int(input("Dime tu edad: "))
except ValueError:  # por si no se ponen enteros:
    print("No has introducido un nº entero...")
else:
    if numero >= 18:
        print("Eres mayor de edad.")
    else:
        print("No eres mayor de edad.")
        
# se puede añadir un último bloque que siempre se ejecuta:
finally:
    print("El programa se ha tetrminado.")