'''
Simplemente se abrirá una ventana
'''

import pygame

# ahora hay que inicializar los módulos:
pygame.init()

# creamos una ventana
ventana = pygame.display.set_mode((800, 600))

# ponemos fondo blanco
ventana.fill((255, 255, 255)) # RGB
#... y actualizamos para que se muestre
pygame.display.update()

# pausamos kla pantalla durante 3 segundos
pygame.time.delay(3000)

# cerramos los módulos para salir sin errores
pygame.quit()