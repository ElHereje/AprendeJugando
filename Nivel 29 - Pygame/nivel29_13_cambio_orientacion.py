'''
Entre este apartado y el siguiente, vamos a mejorar el aspecto de los objetos, 
tanto de la nave como del asteroide.
En el caso de la nave, será superponiendo 2 cuadrados negros mas pequeños
En el siguiente video se trata el movimiento del asteroide, que será
de rotación
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

# 3 - CREAMOS LA FUNCIÓN NAVE CON SUS DIBUJOS (UNA POR CADA DIRECCIÓN)
def nave_arriba(superficie, x, y):
    pygame.draw.rect(superficie, VERDE, (x, y, 60, 60))
    pygame.draw.rect(superficie, NEGRO, (x, y, 15, 30))
    pygame.draw.rect(superficie, NEGRO, (x+45, y, 15, 30))

def nave_abajo(superficie, x, y):
    pygame.draw.rect(superficie, VERDE, (x, y, 60, 60))
    pygame.draw.rect(superficie, NEGRO, (x, y+30, 15, 30))
    pygame.draw.rect(superficie, NEGRO, (x+45, y+30, 15, 30))

def nave_dcha(superficie, x, y):
    pygame.draw.rect(superficie, VERDE, (x, y, 60, 60))
    pygame.draw.rect(superficie, NEGRO, (x+30, y, 30, 15))
    pygame.draw.rect(superficie, NEGRO, (x+30, y+45, 30, 15))

def nave_izq(superficie, x, y):
    pygame.draw.rect(superficie, VERDE, (x, y, 60, 60))
    pygame.draw.rect(superficie, NEGRO, (x, y, 30, 15))
    pygame.draw.rect(superficie, NEGRO, (x, y+45, 30, 15))

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

# 5 - DEFINIMOS UNA VARIABLE DIRECCIÓN
direccion = "arriba" # por defecto, la navi mira hacia arriba

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
                direccion = "derecha"
                nave_vel_x = 10
            if event.key == pygame.K_LEFT:
                direccion = "izquierda"
                nave_vel_x = -10
            if event.key == pygame.K_DOWN:
                direccion = "abajo"
                nave_vel_y = 10
            if event.key == pygame.K_UP:
                direccion = "arriba"
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

    # # 2 TRASLADAMOS ESTO A UNA FUNCIÓN ANTES DEL BUCLE PPAL
    # pygame.draw.rect(ventana, VERDE, (nave_x, nave_y, 60, 60))
    # # 1 - dibujamos los 2 cuadros negros mas pequeños de la nave
    # pygame.draw.rect(ventana, NEGRO, (nave_x, nave_y, 15, 30))
    # pygame.draw.rect(ventana, NEGRO, (nave_x + 45, nave_y, 15, 30))
    
    # 4 - llamamos a la función creada...dependiendo de la direccón
    # se coloca con elif porque SON EXCLUYENTES
    if direccion == "arriba":
        nave_arriba(ventana, nave_x, nave_y)
    elif direccion == "abajo":
        nave_abajo(ventana, nave_x, nave_y)
    elif direccion == "derecha":
        nave_dcha(ventana, nave_x, nave_y)
    elif direccion == "izquierda":
        nave_izq(ventana, nave_x, nave_y)
    
    
    # Actualizamos
    pygame.display.update()
    
# salimos
pygame.quit()