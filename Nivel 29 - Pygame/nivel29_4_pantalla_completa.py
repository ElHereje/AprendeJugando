'''
Resumen de todo lo anterior y configuración de ventana a 
pantalla completa.
'''

import pygame

#Inicializamos
pygame.init()

#Medidas
ALTO = 720
ANCHO = 1280

#Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#Lienzo y configuraciópn a pantalla completa
ventana = pygame.display.set_mode((ANCHO, ALTO), pygame.FULLSCREEN)

#Bucle ppal
jugando = True

while jugando:

    #Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
        #ESC para cerrar
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                jugando = False

    #Dibujos y relleno
    ventana.fill(NEGRO)

    #Actualizamos
    pygame.display.update()

#Salimos
pygame.quit()