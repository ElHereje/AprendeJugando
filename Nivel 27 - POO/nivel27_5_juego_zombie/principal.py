from persona import Persona
from zombi import Zombi
import os

class Principal:
    os.system("cls")
    
    # creamos uas introducción y a continuación, el objeto persona para el jugador
    print()
    print(" La ciudad se ha llenado de zombis.")
    print(" Estás en la calle 1 y has de llegar")
    print(" a la calle 40 para poder salvarte.")
    print()
    print(" Los zombis avanzan 1, 2 ó 3 calles.")
    print(" Tú puedes avanzar 1, 2 ó 3 calles.")
    print()
    nombre = input(" ¿Estás preparado? Cual es tu nombre: ").capitalize()
    
    # creamos el objeto persona para el jugador
    jugador = Persona(nombre)
    
    # creamos los 10 zombis y los incluimos en la lista "horda"
    horda = []
    for i in range(10):
        z = Zombi()
        horda.append(z)
    
    # bucle ppal
    while True:
        
        os.system("cls")
        
        # llamamos al métdodo situación
        print(jugador.situacion())
        
        # mostramos las calles en las que están los zombis
        calles = []
        for zombi in horda:
            calles.append(zombi.calle)
        # .. y los ordenamos..
        calles.sort()
        print("Hay zombis en las calles:")
        for elemento in calles:
            print(elemento, end=" ") # el end es para que no camie de linea...
        print()
        print()
        
        # si el jugador gana
        if jugador.calle > 40:
            print(" No te ha visto ningún zombi.")
            print(" Te has librado de ser comido.")
            print()
            break
        
        # si coincide con un zombi...
        comido = False
        for zombi in horda:
            if zombi.calle == jugador.calle:
                comido = True
        if comido:
            print(" Un zombi te acaba de ver.")
            print(" Te va ha comer. Se acabó el juego.")
            print()
            break
        
        # velocidad del jugador.
        velocidad = ""
        while velocidad not in ("1", "2", "3"):
            velocidad = input(" Cuanto quieres correr (1/2/3): ")
        jugador.moverse(velocidad)
        
        # movimiento de los zombis
        for z in list(horda):
            z.moverse()
            # para eliminar los que se salen de los limites:
            if z.no_visible():
                horda.remove(z)
            # !!! usamos un list para que elimine TODOS los que se salen, 
            # haciendo una copia de la lista horda