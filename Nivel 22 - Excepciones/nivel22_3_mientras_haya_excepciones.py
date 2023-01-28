'''
usar el programa anterior y hacer que se sigua ejecutando
hasta que la entrada sea correcta

try:
    numero = int(input("Dime tu edad: "))
except ValueError:  # por si no se ponen enteros:
    print("No has introducido un nº entero...")
else:
    if numero >= 18:
        print("Eres mayor de edad.")
    else:
        print("No eres mayor de edad.")

'''

# correcto = False
# while not correcto:
#     try:
#         numero = int(input("Dime tu edad: "))
#     except ValueError:  # por si no se ponen enteros:
#         print("No has introducido un nº entero...")
#     else:
#         if numero >= 18:
#             print("Eres mayor de edad.")
#         else:
#             print("No eres mayor de edad.")
#         correcto = True

'''
Una segunda versión es repetirlo pero con 3 intentos
'''

intentos = 0
while True:
    try:
        numero = int(input("Dime tu edad: "))
    except ValueError:  # por si no se ponen enteros:
        intentos += 1
        if intentos < 3:
            print("No has introducido un nº entero...")
        else:
            print("Tres intentos fallidos. Salimos del programa...")
            break
    else:
        if numero >= 18:
            print("Eres mayor de edad.")
        else:
            print("No eres mayor de edad.")
        break
