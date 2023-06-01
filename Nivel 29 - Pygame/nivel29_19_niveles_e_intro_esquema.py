'''
Añadimos ventana de intro y varios niveles

                MISIÓN A JUPITER

tras meses de viaje en misión a Júpiter ya solo se 
interponen en tu camino tres cinturones de asteroides
que te dificultan el paso y amenazan con no dejarte pasar.
Intenta traspasarlos para conseguir finalizar tu misión.

            Pulsal 'ENTER' para comenzar

            ----------------------------------

No has conseguido llegar a Júpiter. Los cinturones
de asteroides han destruido tu nave. Pero has teniodo 
suerte y te han recogido unos chatarreros del espacio.
¿Quieres volverlo a internat a bordo de una nueva nave?

        Pulsa 's' para volverlo a intentar
        Pulsa 'n' para salir del juego

            -----------------------------------

Has conseguido llegar a Júpiter y completar tu misión.
Los cinturones de astreroides no han conseguido parate.
Te has convertido en un héroe del espacio.
¿Quieres embarcarte en una nueva misión?

        Pulsa 's' para volverlo a intentar
        Pulsa 'n' para salir del juego



ESQUEMA:    
while en_juego:
    (while en_inicio)

    while en_partida:
        (while en_nivel)
        (while en_final)   

'''

en_juego = True
while en_juego:
    num_vidas = 3
    num_nivel = 1

    en_partida = False
    en_inicio = True

    while en_inicio:
        # Evento Entrar: partida = True
        # Evento Cerrar ventana:
            # en_inicio = False
            # en_juego = False

    while en_partida:
        en_final = False
        # se crean los asteroides según nivel
        en_nivel = True

        while en_nivel:
            # Evento Cerrar ventana:
                # en_nivel = False
                # en_partida = false
                # en_juego = False
            # Eventos Moverse

            if # colision:
                num_vidas -= 1
                en_nivel = False
            
            if # llegar arriba:
                num_nivel += 1
                en_nivel = False
            
            if num_vidas == 0:
                en_final = True

            if num_nivel > 3:
                en_final = True

        while en_final:
            # Evento Cerrar ventana o no jugar mas:
                # en_final = False
                # en_partida = False
                # en_juego = False
            # Evento jugar de nuevo:
                # en_final = False
                # en_partida = False

            if ganando:
                # mensaje: Se ha gabnado
            else:
                # mensaje = se ha perdido



