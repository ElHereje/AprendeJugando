'''
En este cap. vamos a dar animacion al asteroide, para que parezca que va dando
vueltas.
Se va a realizar con 4 funciones que srepresenten los estados del asteroide rotando 
mediante un contador de frames, que cambiará una figura por otra a unos determinados
frames
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

# FUNCIÓN NAVE CON SUS DIBUJOS (UNA POR CADA DIRECCIÓ
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
    
    
# 1 - definimos 4 funciones para el asteoide
def asteroide_1(superficie, x, y):
    pygame.draw.rect(superficie, NARANJA, (x, y, 60, 60))
    # añadimos un cuadrado negro mas pequeño pero con las mismas coordenadas
    pygame.draw.rect(superficie, NEGRO, (x, y, 20, 20))
    
def asteroide_2(superficie, x, y):
    pygame.draw.rect(superficie, NARANJA, (x, y, 60, 60))
    pygame.draw.rect(superficie, NEGRO, (x+40, y, 20, 20))
    
def asteroide_3(superficie, x, y):
    pygame.draw.rect(superficie, NARANJA, (x, y, 60, 60))
    pygame.draw.rect(superficie, NEGRO, (x+40, y+40, 20, 20))
    
def asteroide_4(superficie, x, y):
    pygame.draw.rect(superficie, NARANJA, (x, y, 60, 60))
    pygame.draw.rect(superficie, NEGRO, (x, y+40, 20, 20))
    
    
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


direccion = "arriba" # por defecto, la navi mira hacia arriba

# 3 - añadimo un contador
contador = 0

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
    
    # 4 - aumentamos la variable contador en 1
    contador += 1
    # 5 para controlar los cambios:
    if contador >= 41:
        contador = 1 # reseteamos contador al llegar a 41
        
    if contador < 11: # a menor nº, aparenta mayor velocidad
        asteroide_1(ventana, aste_x, aste_y)
    elif contador < 21:
        asteroide_2(ventana, aste_x, aste_y)
    elif contador < 31:
        asteroide_3(ventana, aste_x, aste_y)
    elif contador < 41:
        asteroide_4(ventana, aste_x, aste_y)
        
        
    # 2- movemos la sentencia a la funcion asteroide
    # pygame.draw.rect(ventana, NARANJA, (aste_x, aste_y, 60, 60))

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