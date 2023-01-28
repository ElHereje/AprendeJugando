'''
Como ejemplo vamos optimizar un programa que lleva a cabo una división

dividendo = float(input("Introduce el dividendo: "))
divisor = float(input("Introduce el divisor: "))
resultado = dividendo / divisor
print(resultado)

No se puede dividir entre 0 --> ZeroDivisionError
Valores incorrectos --> ValueError

'''
while True:
    try:
        dividendo = float(input("Introduce el dividendo: "))
        divisor = float(input("Introduce el divisor: "))
        resultado = dividendo / divisor
    except ValueError:
        print("No has introducido datos correctos")
    except ZeroDivisionError:
        print("No se puede dividir entre cero.")
    # podríamos haber impreso la excepcion que se lanza con:
    # except BaseException as error:
    #     print(error)  --> para capturar excepciones que no esperamos
    else:
        print(resultado)
        break
