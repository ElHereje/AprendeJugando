'''
Vamos a cdificar que sea el usuario quien mueva las figuras
'''

import pygame

# iniciamos
pygame.init()

# medidas
ANCHO = 1280
ALTO = 720

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
NARANJA = (255, 128, 0)

# ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()

# Datos
aste_x = 100
aste_y = 100
aste_vel_x = 5

nave_x = 600
nave_y = 500
nave_vel_x = 0
nave_vel_y = 0

# BUCLE PPAL
jugando = True
while jugando:
    
    reloj.tick(60)
    
    # eventos
    for  event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                jugando = False
            if event.key == pygame.K_RIGHT:
                nave_vel_x = 10
            if event.key == pygame.K_LEFT:
                nave_vel_x = -10
            if event.key == pygame.K_DOWN:
                nave_vel_y = 10
            if event.key == pygame.K_UP:
                nave_vel_y = -10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                nave_vel_x = 0
            if event.key == pygame.K_LEFT:
                nave_vel_x = 0
            if event.key == pygame.K_DOWN:
                nave_vel_y = 0
            if event.key == pygame.K_UP:
                nave_vel_y = 0
                
                
    # Lógica
    aste_x += aste_vel_x
    if aste_x > ANCHO:
        aste_x = -60
    nave_x += nave_vel_x
    nave_y += nave_vel_y
    
    
    # Dibujos
    ventana.fill(NEGRO)
    pygame.draw.rect(ventana, NARANJA, (aste_x, aste_y, 60, 60))
    pygame.draw.rect(ventana, VERDE, (nave_x, nave_y, 60, 60))
    
    
    # Actualizamos
    pygame.display.update()
    
# salimos de la aplicación.
pygame.quit()