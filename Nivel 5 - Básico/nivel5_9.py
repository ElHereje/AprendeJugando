'''
Programa que pida una contraseña y luego la
repitas 2 veces.
Después comprueba que lo has hecho correctamente
'''

password = input("Introduce una contraseña: ")
pass_a = input("Primera repetición: ")
pass_b = input("Segunda repetición: ")

if password == pass_a == pass_b:
    print(f"Contraseña Correcta")
else:
    print("No coinciden")
