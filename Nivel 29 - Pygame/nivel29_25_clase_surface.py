import pygame

# inicializamos
pygame.init()

# medidas
ANCHO = 1280
ALTO = 720

# Colores
NEGRO = (0, 0, 0)
VERDE = (0, 150, 0)
MARRON = (150, 60, 10)


# Ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))

imagen_manzana = pygame.image.load("Nivel 29 - Pygame\manzana.png").convert_alpha()

# Datos

personaje_rect = pygame.Rect(400, 200, 50, 50)

manzana_rect = imagen_manzana.get_rect()
manzana_rect.x = 600
manzana_rect.y = 400


# Bucle principal
jugando = True
while jugando:

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False


    # Lógica

        
    # Dibujos
    ventana.fill(VERDE)

    pygame.draw.rect(ventana, MARRON, personaje_rect)

    # pegamos superficie manzana sobre la superficie ventana
    ventana.blit(imagen_manzana, manzana_rect)

    # Actualizar
    pygame.display.update()


# Salir
pygame.quit()