'''
FPS - frames por segundo
VAmos a ver otra forma de relkentizar los movimientos, antes vistos con delay()., creando
un objeto de tipo reloj
'''

import pygame
import random

# medidas

ANCHO = 800
ALTO = 600

# colores

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

#Inicializamos pygame y la fuente de textos

pygame.init()
ventana = pygame.display.set_mode((ANCHO, ALTO))
fuente = pygame.font.SysFont("arial", 64)

#1 - CREAMOS EL RELOJ
reloj = pygame.time.Clock()


# Datos

# creamos 50 cuadrados
cuadrados = []
for i in range(50): # a mayor nº de cuadros, menos fps
    x = random.randint(1, 799)
    y = random.randint(1, 599)
    c = [x, y]
    cuadrados.append(c)
    
#2 - iniciamos los frames a 0
frames = 0
transcurrido = 0
fps = 0
segundos = 0

# Bucle ppal

jugando = True
while jugando:
    
    #3 -  iniciamos la variable tiempo e incrementamos los frames
    tiempo = reloj.tick(60) # limitamos la vel. a 60 fps
    transcurrido += tiempo
    frames += 1
    if transcurrido >= 1000: # por cada segundo...
        fps = frames # recogemos los frames en ese segundo
        frames = 0 # reseteamos los frames
        segundos += 1 # sumamos los segundos transcurridos
        transcurrido = 0 #reseteamos transcurrido

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    # Lógica
    # pàra cada cuadrado, aumentamnos x en 1 e y en 2
    for c in cuadrados:
        c[0] += 1
        c[1] += 2
        if c[0] > 800:
            c[0] = 0
        if c[1] > 600:
            c[1] = 0

    # Imagenes
    ventana.fill(NEGRO)

    for c in cuadrados:
        pygame.draw.rect(ventana, BLANCO, (c[0], c[1], 10, 10)) 
        
    #4 - Insertamos 2 textos...
    texto1 = fuente.render(str(fps), True, BLANCO)
    texto2 = fuente.render(str(segundos), True, BLANCO)
    ventana.blit(texto1, (80, 100))
    ventana.blit(texto2, (600, 100))

    # Update
    pygame.display.update()

pygame.quit()
