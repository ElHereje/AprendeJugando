'''
Vamos a poner distintos asteroides, cada uno con su vel.
y se choca con la nave, colisiones
'''


import pygame, random

# inicializar
pygame.init()

#medidas
ANCHO = 1280
ALTO = 720

#colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# 1 - definimos la función colisión.
def colision(x1, y1, a1, b1, x2, y2, a2, b2, ex=0):
    if x1 + a1 > x2 + ex and \
       x1 + ex < x2 + a2 and \
       y1 + b1 > y2 + ex and \
       y1 + ex < y2 + b2:
        return True
    else:
        return False

#ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()
fuente = pygame.font.SysFont("arial black", 20)

# 2 - cargamos todas las imagenes
fondo = pygame.image.load("./images/fondo.png")

nave_arriba = pygame.image.load("./images/nave_arriba.png").convert_alpha()
nave_abajo = pygame.image.load("./images/nave_abajo.png").convert_alpha()
nave_izquierda = pygame.image.load("./images/nave_izquierda.png").convert_alpha()
nave_derecha = pygame.image.load("./images/nave_derecha.png").convert_alpha()

# asteroide grande
aste_1a = pygame.image.load("./images/asteroide_1a.png").convert_alpha()
aste_1b = pygame.image.load("./images/asteroide_1b.png").convert_alpha()
aste_1c = pygame.image.load("./images/asteroide_1c.png").convert_alpha()
aste_1d = pygame.image.load("./images/asteroide_1d.png").convert_alpha()

# definimos 4 asteroides dif, con didtinto orden, para que no roten
#con el mismo orden
aste_1 = [aste_1a, aste_1b, aste_1c, aste_1d]
aste_3 = [aste_1b, aste_1c, aste_1d, aste_1a]
aste_4 = [aste_1c, aste_1d, aste_1a, aste_1b]
aste_5 = [aste_1d, aste_1a, aste_1b, aste_1c]

# igual pero con el pequeño
aste_2a = pygame.image.load("./images/asteroide_2a.png").convert_alpha()
aste_2b = pygame.image.load("./images/asteroide_2b.png").convert_alpha()
aste_2c = pygame.image.load("./images/asteroide_2c.png").convert_alpha()
aste_2d = pygame.image.load("./images/asteroide_2d.png").convert_alpha()

aste_2 = [aste_2a, aste_2b, aste_2c, aste_2d]
aste_6 = [aste_2b, aste_2c, aste_2d, aste_2a]
aste_7 = [aste_2c, aste_2d, aste_2a, aste_2b]
aste_8 = [aste_2d, aste_2a, aste_2b, aste_2c]


# creamos los asteroides
asteroides_grandes = []
asteroides_pequenios = []

for i in range(10): # creamos primero 10 asteroides
    x = random.randint(0, ANCHO)
    y = random.randint(50, ALTO-120)
    v = random.randint(1, 3)
    f = random.choice([aste_1, aste_3, aste_4, aste_5])
    a = [f, x, y, v]
    asteroides_grandes.append(a)

for i in range(10):
    x = random.randint(0, ANCHO)
    y = random.randint(50, ALTO-120)
    v = random.randint(1, 4)
    f = random.choice([aste_2, aste_6, aste_7, aste_8])
    a = [f, x, y, v]
    asteroides_pequenios.append(a)

asteroides = asteroides_grandes + asteroides_pequenios


# Datos
vidas = 3
nivel = 1
nave_pos_x = 600
nave_pos_y = 670
nave_vel_x = 0
nave_vel_y = 0
direccion = "arriba"

# contamos los frames para cambiar la imagen del asteroide
frames_asteroides = 0

jugando = True

while jugando:

    reloj.tick(60)

    #Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                jugando = False
            if event.key == pygame.K_RIGHT:
                direccion = "derecha"
                nave_vel_x = 2
            if event.key == pygame.K_LEFT:
                direccion = "izquierda"
                nave_vel_x = -2
            if event.key == pygame.K_DOWN:
                direccion = "abajo"
                nave_vel_y = 2
            if event.key == pygame.K_UP:
                direccion = "arriba"
                nave_vel_y = -2
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
    for a in asteroides_grandes:
        a[1] += a[3] # aumentamos la vel
        if a[1] > ANCHO:
            a[1] = -64
            
    for a in asteroides_pequenios:
        a[1] += a[3]
        if a[1] > ANCHO:
            a[1] = -32        
    
    
    nave_pos_x += nave_vel_x
    nave_pos_y += nave_vel_y

    if nave_pos_x > ANCHO - 32:
        nave_pos_x = ANCHO - 32
    if nave_pos_x < 0:
        nave_pos_x = 0
    if nave_pos_y > ALTO - 32:
        nave_pos_y = ALTO - 32
    if nave_pos_y < 10 : # HEMOS GANADO
        jugando = False 

    for a in asteroides_grandes: # comprobamos colisiones
        if colision(a[1], a[2], 64, 64, nave_pos_x, nave_pos_y, 32, 32, 15):
            jugando = False

    for a in asteroides_pequenios:
        if colision(a[1], a[2], 32, 32, nave_pos_x, nave_pos_y, 32, 32, 15):
            jugando = False

    # Imagenes
    ventana.blit(fondo, (0, 0))
    texto1 = fuente.render("Nivel: " + str(nivel), True, BLANCO)
    texto2 = fuente.render("Vidas: " + str(vidas), True, BLANCO)
    ventana.blit(texto1, (20, 10))
    ventana.blit(texto2, (1150, 10))

    frames_asteroides += 1
    if frames_asteroides >= 41:
        frames_asteroides = 1

    if frames_asteroides < 11:
        for a in asteroides: # colocamos la imagen dependiendo de los frames
            ventana.blit(a[0][0], (a[1], a[2]))
    elif frames_asteroides < 21:
        for a in asteroides:
            ventana.blit(a[0][1], (a[1], a[2]))
    elif frames_asteroides < 31:
        for a in asteroides:
            ventana.blit(a[0][2], (a[1], a[2]))
    elif frames_asteroides < 41:
        for a in asteroides:
            ventana.blit(a[0][3], (a[1], a[2]))

    if direccion == "arriba":
        ventana.blit(nave_arriba, (nave_pos_x, nave_pos_y))
    if direccion == "abajo":
        ventana.blit(nave_abajo, (nave_pos_x, nave_pos_y))
    if direccion == "izquierda":
        ventana.blit(nave_izquierda, (nave_pos_x, nave_pos_y))
    if direccion == "derecha":
        ventana.blit(nave_derecha, (nave_pos_x, nave_pos_y))

    pygame.display.update()

pygame.quit()
