'''
Vamos a usar el método CONVERT, que transforma el formato de pixeles de la imagen
para que sea mas rápido mostrarlas.
(usaremos CONVERT_ALPHA si hay transparencias).
Esto se hace en la misma linea quie se carga
'''


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

# 1 - usamos convert al cargar las imagenes
fondo = pygame.image.load("./images/fondo.png")
asteroide_1a = pygame.image.load("./images/asteroide_1a.png").convert()
asteroide_1a.set_colorkey(BLANCO)
asteroide_2a = pygame.image.load("./images/asteroide_2a.png").convert_alpha()
nave_arriba = pygame.image.load("./images/nave_arriba.png").convert_alpha()

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
    ventana.blit(fondo, (0, 0))
    ventana.blit(asteroide_1a, (200, 200))
    ventana.blit(asteroide_2a, (600, 400))
    ventana.blit(nave_arriba, (600, 500))

    pygame.display.update()

pygame.quit()