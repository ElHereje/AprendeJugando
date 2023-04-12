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
    
    # Introducimos opción para el nº de jugadores
    numero = ""
    while numero not in ("1", "2", "3", "4"):
        numero = input(" Número de jugadores (1/4): ")

    # creamos la lista de los jugadores
    jugadores = []
    for i in range(1, int(numero) + 1):
        nombre = input(" Nombre del " + str(i) +"º jugador: ").capitalize()
        # creamos un objeto Persona por cada jugador
        jugador = Persona(nombre)
        # añadimos ese objeto a la lista jugadores
        jugadores.append(jugador)
    
    horda = []
    for i in range(10):
        z = Zombi()
        horda.append(z)
    
    # bucle ppal (controlamos que queden jugadores)
    while len(jugadores) > 0:
        
        os.system("cls")
        
        # mostramos la tabla de situación
        print(" NOMBRE    -   CALLE   -   ENERGIA")
        print(" ---------------------------------")
        for jugador in jugadores:
            nom, cal, ene = jugador.situacion()
            print("  {:8}  -   {:2}     -     {:2}".format(nom, cal, ene))
        print()
        
        # mostramos las calles en las que están los zombis
        calles = []
        for zombi in horda:
            calles.append(zombi.calle)
        # .. y los ordenamos..
        calles.sort()
        print("Hay zombis en las calles:")
        for elemento in calles:
            print(elemento, end=" ") # el end es para que no cambie de linea...
        print()
        print()
        
        # si los jugadores ganan:
        ganadores = []
        for jugador in jugadores:
            if jugador.calle >= 40:
                ganadores.append(jugador)
        if len(ganadores) > 0:
            for jugador in ganadores:
                print(f" {jugador.nombre}, has escapado de los zombis.")
            print(" Has/Habeis ganado la partida.")
            print()
            break

        # Ahora introducimos la gestión de la energía
        for jugador in list(jugadores): # creamos una lista para poder eliminar jugadores
            if jugador.energia <= 0:
                print(f" {jugador}, has perdido toda la energía. Estás comido...")
                jugador.remove(jugador)

        
        # si algún jugador coincide con un zombi...
        for jugador in list(jugadores): # creamos una lista para poder eliminar jugadores
            for zombi in horda:
                if zombi.calle == jugador.calle:
                    if jugador in jugadores:
                        print(f" {jugador.nombre}, un zombi te acaba de ver. Has perdido")
                        jugadores.remove(jugador)
        

        # velocidad de los jugadores.
        print()
        for jugador in list(jugadores):
            velocidad = ""
            while velocidad not in ("1", "2", "3"):
                velocidad = input(f" {jugador.nombre}, cuanto quieres correr (1/2/3): ")
            jugador.moverse(velocidad)
        

        # movimiento de los zombis
        for z in list(horda):
            z.moverse()
            # para eliminar los que se salen de los limites:
            if z.no_visible():
                horda.remove(z)
            # !!! usamos un list para que elimine TODOS los que se salen, 
            # haciendo una copia de la lista horda
    
    else:
        print(" Todos han sido comidos. No hay ganadores.")
        print()
