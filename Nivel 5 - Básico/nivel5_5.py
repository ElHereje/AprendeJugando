# Indicar si un número es múltiplo de 3 o 5 o de los 2

num = int(input("Dime otro número: "))
'''if (num % 5 == 0) and (num % 3 == 0):
    print(f"El número {num} es múltiplo de 3 y 5")
elif num % 3 == 0 :
    print(f"El número {num} es múltiplo de 3")
elif num % 5 == 0 :
    print(f"El número {num} es múltiplo de 5")
else:
    print(f"El número {num} no es múltiplo de ninguno")'''

if num % 3 == 0 :
    if num % 5 == 0:
        print(f"El número {num} es múltiplo de 3 y de 5")
    else:
        print(f"El número {num} es múltiplo de 3")
else:
    if num % 5 == 0:
        print(f"El número {num} es múltiplo de 5")
    else:
        print(f"El número {num} no es múltiplo de ninguno")