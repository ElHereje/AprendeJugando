"""
Haz un programa con una función que muestre un saludo
dando la bienvenida al usuario, usando su nombre, el cual
se ha pedido antes de llamar a la función.
La función devuelve None. (return None, aunque no es necesario)
Definir la función con un parámetro (nombre de usuario)
"""

def saludo(nombre):

    print(f"Hola {nombre}, Bienvenido al programa.")
    print("Muchas gracias por participar")
    print(f"Espero que lo pase bien, {nombre}.")

    return  None

nom = input("Introduzca su nombre: ")
saludo(nom)