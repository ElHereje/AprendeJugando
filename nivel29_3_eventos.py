import pygame

pygame.init()

# cxreamos 2 ctes para guardar constantes
ANCHO = 800
ALTO = 600
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

ventana = pygame.display.set_mode((ANCHO, ALTO))

# creamos un bucle para cerrar cuando acabemos
jugando = True

while jugando:

    # recogemos eventos...
    for event in pygame.event.get():
        
        # para ver en consola los eventos que ocurren...
        #print(event)

        # para cerrar:
        if event.type == pygame.QUIT:
            jugando = False

        # para salir si se pulsa la tecla Q
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                jugando = False


    # rellenamso con color
    ventana.fill(ROJO)
    # ... y actualizamos
    pygame.display.update()

pygame.quit()

