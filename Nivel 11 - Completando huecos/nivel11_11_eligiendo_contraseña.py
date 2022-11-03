"""
Hacer un programa en el que haya que elegir una contraseña.
Esta ha de tener entre 8 y 15 caracteres, 1 mayúscula,
1 minúscula 1 dígito, 1 carácter especial: @$%&

Habrá 5 intentos de establecer la contraseña, después de cada
intento se indicará la causa si ha sido fallida y al final
del quinto intento se indicará que no ha sido posible
establecer la contraseña.
"""


posibles_may = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
posibles_min = "abcdefghijklmnñopqrstuvwxyz"
posibles_num = "0123456789"
posibles_esp = "@$%&"
intentos = 0
eligiendo = True
password = None

while eligiendo:
    intentos += 1
    intento_password = input("Introduce una contraseña: ")

    lon = False
    may = False
    min = False
    num = False
    esp = False

    # comprobamos la longitud
    if len(intento_password) > 7 and len(intento_password) < 16:
        lon = True

    # comprobamos los caracteres exigidos
    for caracter in intento_password:
        if caracter in posibles_may:
            may = True
        if caracter in posibles_min:
            min = True
        if caracter in posibles_esp:
            esp = True
        if caracter in posibles_num:
            num = True

    # si todo es correcto...
    if lon and may and min and min and num and esp:
        print("La contraseña se ha elegido correctamente.")
        # le damos su valor a la contraseña...
        password = intento_password
        # ... y alteramos la bandera para salir del bucle
        eligiendo = False

    # si no, indicamos el motivo
    else:
        # elif porque solo mostraremos uno de los mensajes...
        if not lon:
            print("La contraseña no cumple la longitud indicada.")
        elif not may:
            print("Debe tener al menos una MAYÚSCULA")
        elif not min:
            print("Debe tener al menos una MINÚSCULA")
        elif not num:
            print("Debe tener al menos un NÚMERO")
        elif not esp:
            print("Debe tener al menos un CARÁCTER ESPECIAL")

    if intentos > 4:
        eligiendo = False

# Si todo ha sido correcto...
if password:
    print(f"Su contraseña es: {password}.")
# si un error nos ha hecho salir del bucle ( condiciones o intentos... )
else:
    print("no se ha podido establecer su contraseña...")



