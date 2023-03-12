'''
Programa que pida contraseña y no deje pasar
hasta que la pongas correctamente
'''

contrasenia = "1234"
print("BIENVENIDO AL SISTEMA\n")
intento = input("Introduce una contraseña: ")
while contrasenia != intento:
    print("CONTRASEÑA INCORRECTA")
    intento = input("Inténtelo de nuevo: ")
print("Contraseña Correcta\n")
print("ACCESO PERMITIDO")