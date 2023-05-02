# en resumen, podemos resumir lo visto hasta ahora
import pygame

#inicializamos
pygame.init()

#medidas
ANCHO = 1280
ALTO = 720

#colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#Ventana a pantalla copleta
ventana = pygame.display.set_mode((ANCHO, ALTO), pygame.FULLSCREEN)

#Bucle ppal
jugando = True
while jugando:
    
    #Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
        #ESC para cerrar
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                jugando = False
                
    #Dibujos
    ventana.fill(NEGRO)
    
    #Actualizar
    pygame.display.update()
    
#Salir
pygame.quit()

    
    