# DENTRO DEL INTERVALO


'''
Juego 'Ruleta de Colores'
1. El juego nos pide un color
2. Si acertamos, nos da 1 pto y pide otro color
3. Si no acertamos, nos da lo conseguido y se acaba
'''


colores = ('rojo', 'blanco', 'lila', 'azul', 'verde')
puntos = 0
jugando = True
while jugando:
    color = input("Dime un color: ")
    if color in colores:
        puntos += 1
        print(f"Correcto, sumas 1 punto. Ahora tienes {puntos} puntos\n")
    else:
        jugando = False
        print(f"El {color} no está en la lista.")
        print(f"Has conseguido {puntos} puntos\n")
        print("FIN DEL JUEGO")
