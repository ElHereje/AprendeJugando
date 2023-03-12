'''
Programa que pida usuario y contraseña y no deje pasar
hasta que se pongan correctamente
'''

'''usuario = "pepe"
contrasenia = "1234"
print("BIENVENIDO AL SISTEMA\n")
intento_usu = input("Introduce usuario: ")
intento_contra = input("Introduce contraseña: ")
while (contrasenia != intento_contra) or (intento_usu != usuario):
    print("DATOS INCORRECTOS")
    intento_usu = input("Introduce usuario: ")
    intento_contra = input("Introduce contraseña: ")
print("Datos Correctos\n")
print("ACCESO PERMITIDO")'''

# Igual, pero usando "banderas"

usuario = "pepe"
contrasenia = "1234"
print("BIENVENIDO AL SISTEMA\n")
entrando = False  # <-- esta es la bandera
while not entrando:
    intento_usu = input("Introduce usuario: ")
    intento_contra = input("Introduce contraseña: ")
    if (contrasenia == intento_contra) and (intento_usu == usuario):
        print("Datos Correctos\n")
        entrando = True
    else:
        print("DATOS INCORRECTOS")

print("ACCESO PERMITIDO")