'''
-------------------------
    GENERADOR DE TEST
-------------------------
1. Entrar al sistema
2. Darse de alta
3. salir
-------------------------

al acceder solicita credenciales

Una vez hemos accedido:

-------------------------
    USUARIO: imad
-------------------------
1. Hacer un test
2. Puntuaciones
3. Salir
-------------------------

Se va arealizar con funciones, ya que el programa tiene 
diversas opciones

'''

import random
import os

def listar_usuarios():
    '''Abre el archivo donde están los usuarios y sus datos, y guarda
    los datos en una lista para su posterior uso'''
    
    with open("datos.txt", "r") as archivo_datos:
        lista_datos = archivo_datos.readlines()
        
    lista_usuarios = []
    for dato in lista_usuarios:
        #strip quita los saltos de linea y split crea una lista
        lista_usuarios.append(dato.strip().split(","))
        
    return lista_usuarios


def menu_entrada():
    '''Menú de entrada'''
    
    print("--------------------------")
    print("    GENERADOR DE TEST")
    print("--------------------------")
    print("1. Entrar al sistema")
    print("2. Darse de alta")
    print("3. salir")
    print("--------------------------")
    opcion = ""
    while opcion not in ("1", "2", "3"):
        opcion = input("--> ")
    return opcion


def menu_principal(nombre_usuario):
    '''Menú una vez dentro del sistema'''
    
    print("--------------------------")
    print(F"    USUARIO: {nombre_usuario}")
    print("--------------------------")
    print("1. Hacer test")
    print("2. Puntuaciones")
    print("3. salir")
    print("--------------------------")
    opcion = ""
    while opcion not in ("1", "2", "3"):
        opcion = input("--> ")
    return opcion


def entrar_al_sistema(lista_usuarios):
    '''Pide user y pass y comprueba que los datos son 
    correctos en la bbdd de usuarios'''
    
    usr = input(" Introduce usuario: ")
    con = input(" Introduce contraseña: ")
    
    for usuario in lista_usuarios:
        if usuario[0] == usr and usuario[1] == con:
            return usuario
    else:
        return None
        
    
def darse_de_alta(lista_usuarios):
    '''Pide usr y pass para dar de alta al usuario'''
    
    while True:
        usr = input(" Elige usuario: ")
        if len(usr) < 4:
            print(" ha de tener al menos 4 caracteres")
        # si está bién escrito...
        else:
            for usuario in lista_usuarios:
                if usr == usuario[0]:
                    print(" Ese nombre está cogido")
                    break
                # si no está repetido...    
            else:
                while True:
                    con1 = input(" Elige contraseña: ")
                    if len(con1) < 4:
                        print(" ha de tener al menos 4 caracteres")
                    else:
                        con2 = input(" Repite contraseña: ")
                        if con1 != con2:
                            print(" las contraseñas no coinciden")
                            break
                        # si las contraseñas coinciden, se guardan en la lista
                        else:
                            lista_usuarios.append([usr, con1, "0", "0", "0"])
                            print(" Usuario dado de alta.")
                            
                            return lista_usuarios
                            
                            
def grabar_datos(lista_usuarios):
    '''guarda los datos de usuario en el archivo de texto.
    No devuelve nada, solo graba'''
    
    with open("datos.txt", "w") as archivo_datos:
        for u in lista_usuarios:
            # escribimos una linea en el archivo...
            archivo_datos.write(u[0] + "," + u[1] + "," + u[2] + "," + u[3] + "," + u[4] + "\n")
    return None


def test():
    '''Genera un test de matemáticas simple (suma de numeros aleatorios)'''
    
    puntos = 0
    
    # van a ser 5 preguntas
    for i in range(5):
        # limpiamos pantalla en cada pregunta
        os.system("cls")
        
        print("--------------------------")
        print(f"     Pregunta {i+1}")
        print("--------------------------")
        
        op1 = random.randint(1, 9)
        op2 = random.randint(1, 9)
        pregunta = int(input(f" {op1} + {op2} ="))
        
        if pregunta == op1 + op2:
            print()
            print("    ¡ Correcto...!")
            puntos += 1
        else:
            print()
            print("    ¡ Incorrecto...!")
        
        print()
        input(" Enter para continuar...")
        
    # acabadas las preguntas, limpiamos pantalla y presentamos resultado
    os.system("cls")
    
    print("--------------------------")
    print(f"     FIN DEL TEST")
    print("--------------------------")
    print()
    print(f" Has conseguido {puntos} puntos.")
    print()
    input(" Enter para continuar...")
    
    # devolvemos los puntos obtenidos
    return puntos


def actualizar_puntos(usuario, puntos):
    """En base a los puntos obtenidos, se actuaclizan los datos de
    veces, mejor y media de un usuario en la lista de sus datos"""
    
    # convertimos en numérico los datos de la cadena de texto de usuario
    # (usr, pass, veces, mejor, media)
    usuario[2] = int(usuario[2])
    usuario[3] = int(usuario[3])
    usuario[4] = float(usuario[4])
    
    # aumentamos el nº de veces jugadas
    usuario[2] += 1
    # actualizamos los puntos con la mejor puntuación
    if puntos > usuario[3]:
        usuario[3] = puntos
    # si es la 1ª vez que se juega, la media serán los puntos
    if usuario[2] == 1:
        usuario[4] = puntos
    # ... de lo contrario, calculamos la media
    else:
        usuario[4] = (usuario[4] + puntos) / 2
        
    # volvemos a convertir en str para guardarlo el el archivo de texto
    usuario[2] = str(usuario[2])
    usuario[3] = str(usuario[3])
    usuario[4] = str(round(usuario[4], 2)) # redondeamos con 2 decimales
    
    #... y devolvemos el usuario ya con todos sus datos
    return usuario


def mostrar_puntuacion(usuario):
    '''Se muestra la puntuación del usuario'''
    
    # limpiamos la pantalla
    os.system("cls")
    
    # presentamos la puntuación
    print("--------------------------")
    print(f"    PUNTUACIONES : {usuario[0]}")
    print("--------------------------")
    print("   Veces | Mejor | Media ")
    print(f"     {usuario[2]}   |   {usuario[3]}   |   {usuario[4]}")
    print("--------------------------")
    
    # no se devuelve nada
    return None
    
            





##############  FLUJO DEL PROGRAMA ##############

# si el archivo no existe...
if not os.path.isfile("datos.txt"):
    # lo creamos...
    with open("datos.txt", "w") as archivo_datos:
        pass
    
while True:
    
    jugando = False
    os.system("cls")
    
    lista_usuarios = listar_usuarios()
    opcion_entrada = menu_entrada()
    
    if opcion_entrada == "1":
        usuario = entrar_al_sistema(lista_usuarios)
        if usuario == None:
            input(" Datos incorrectos...")
        else:
            jugando = True
            
    elif opcion_entrada == "2":
        lista_usuarios = darse_de_alta(lista_usuarios)
        grabar_datos(lista_usuarios)
        input(" Enter para continuar...")

    elif opcion_entrada == "3":
        break
    
    # si hemos dado a la opción 1, jugando es True
    while jugando:
        # limpiamos la pantalla
        os.system("cls")
        
        # entramos al siguiente menú
        opcion = menu_principal(usuario[0])
        
        # hacer test
        if opcion == "1":
            puntos = test()
            usuario = actualizar_puntos(usuario, puntos)
            
            # no hace falta actualizar lista_usuarios, porque usuario está
            # vinculado a ella: usuario = lista_usuarios[indice]
            
            grabar_datos(lista_usuarios)
        # puntuaciones    
        elif opcion == "2":
            mostrar_puntuacion(usuario)
            print()
            input(" Enter para continuar...")
        # salir    
        elif opcion == "3":
            jugando = False
