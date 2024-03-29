import pygame

# inicializar
pygame.init()

#medidas
ANCHO = 1280
ALTO = 720

#colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
NARANJA = (255, 128, 0)
VERDE = (0, 255, 0)

#ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()

# 1 -  Cargamos las imagenes
fondo = pygame.image.load("./images/fondo.png")
# 2 -  asociamos los objetos
asteroide_1a = pygame.image.load("./images/asteroide_1a.png")


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

    # Imagenes

    # 2 - insertamos el fondo con corrdenada 0, 0 
    ventana.blit(fondo, (0, 0))

    #pygame.draw.rect(ventana, NARANJA, (200, 200, 60, 60))
    ventana.blit(asteroide_1a, (200, 200))
    pygame.draw.rect(ventana, VERDE, (600, 500, 60, 60))

    pygame.display.update()

pygame.quit()