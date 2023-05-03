'''
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

#Inicializamos pygame

pygame.init()
ventana = pygame.display.set_mode((ANCHO, ALTO))
fuente = pygame.font.SysFont("arial", 64)

#CREAMOS EL RELOJ
reloj = pygame.time.Clock( )


# Datos

# creamos 50 cuadrados
cuadrados = []
for i in range(50):
    x = random.randint(1, 799)
    y = random.randint(1, 599)
    c = [x, y]
    cuadrados.append(c)

# Bucle ppal

jugando = True
while jugando:

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

    # Update
    pygame.display.update()

pygame.quit()

