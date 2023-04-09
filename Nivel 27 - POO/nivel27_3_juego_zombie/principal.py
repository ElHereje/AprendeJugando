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
        
        ''' ahora hay que implementar las distintas situaciones
        * movimientos del jugador
        * que el jugador gane
        * que el jugador pierda  
        '''