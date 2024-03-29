'''
Hasta ahora lo hemos realizado de manera básica, pwero Python ya tiene clases predifinidas
como la clase rect, que guarda coordenadas rectangulares

mi_rectangulo = Rect(400, 300, 50, 50)


'''


import pygame

# Inicializar
pygame.init()

# Medidas
ANCHO = 1280
ALTO = 720

# Colores
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

# Ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()

# Datos

nave = pygame.Rect(600, 500, 50, 50)
nave_vel_x = 0
nave_vel_y = 0


# Bucle principal
jugando = True
while jugando:

    reloj.tick(60)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                jugando = False
            if event.key == pygame.K_RIGHT:
                nave_vel_x = 5
            if event.key == pygame.K_LEFT:
                nave_vel_x = -5
            if event.key == pygame.K_DOWN:
                nave_vel_y = 5
            if event.key == pygame.K_UP:
                nave_vel_y = -5
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

    nave.x += nave_vel_x
    nave.y += nave_vel_y

    if nave.x > ANCHO - nave.width:
        nave.x = ANCHO - nave.width
    if nave.x < 0:
        nave.x = 0
    if nave.y > ALTO - nave.height:
        nave.y = ALTO - nave.height
    if nave.y < 0:
        nave.y = 0
        
    # Dibujos

    ventana.fill(NEGRO)

    pygame.draw.rect(ventana, AZUL, nave)



    # Actualizar
    pygame.display.update()


# Salir
pygame.quit()