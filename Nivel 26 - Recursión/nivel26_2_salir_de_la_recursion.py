'''
Como ejemplo de lo anterior, hacer un programa que cuente
desde m hasta n (hacia delante)
'''

# def cuenta(m, n):
#     if m == n: # caso base
#         print(f"{m} Se acabó...")
#     else:
#         print(m)
#         cuenta(m+1, n)

# cuenta(10, 20)

''' hasta que no se llega al caso base, el flujo del programa no continua,
sino que sigue evaluando hasta que se se llega. Es entonces cuando el flujo
continua'''

def cuenta(m, n):
    if m == n: # caso base
        print("Hemos llegado al caso base", m)
    else:
        print("No hemos llegado al caso base", m)
        cuenta(m+1, n)
        print("Saliendo de la recursión", m)

cuenta(10, 15)