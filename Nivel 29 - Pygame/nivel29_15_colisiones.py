'''
Vamos a ver como gestionar colisiones. Para ello usamos el ejempolo en el que 
solo aparecen 2 cuadros
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

# 1 - Resumimos las funciones
def nave(superficie, x, y, ancho, alto):
    pygame.draw.rect(ventana, VERDE, (x, y, ancho, alto))

def asteroide(superficie, x, y, ancho, alto):
    pygame.draw.rect(ventana, NARANJA, (x, y, ancho, alto))


# ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()

# 2 añadimos los datos de ancho y alto
aste_ancho = 60
aste_alto = 60
aste_x = 100
aste_y = 100
aste_vel_x = 5


nave_ancho = 60
nave_alto = 60
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

    # 4 - progrtamamos las colisiones:
    # añadimos 20 por si no es un cuadrado perfecto...
    if aste_x + aste_ancho > nave_x + 20 and \
        aste_x + 20 < nave_x + nave_ancho and \
        aste_y + aste_alto > nave_y + 20 and \
        aste_y + 20 < nave_y + nave_alto:

        pygame.time.delay(1000)
        aste_x = 100
        aste_y = 100
    
    
    # Dibujos
    ventana.fill(NEGRO)
    # 3 - llamamos a las funciones con los argumentos oportunos:
    asteroide(ventana, aste_x, aste_y, aste_ancho, aste_alto)
    nave(ventana, nave_x, nave_y, nave_ancho, nave_alto)
    
    # Actualizamos
    pygame.display.update()
    
# salimos de la aplicación.
pygame.quit()