# En este video, vamos a dibujar figuras dentro de la ventana 
import pygame

#inicializamos
pygame.init()

#medidas
ANCHO = 800
ALTO = 600

#colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#Ventana a pantalla copleta
ventana = pygame.display.set_mode((ANCHO, ALTO))

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
                
    #Dibujos:
    # fondo...
    ventana.fill(NEGRO) 
    # formas...
    pygame.draw.rect(ventana, VERDE, (10, 10, 100, 100))
    
    #Actualizar (no se refleja nada hasta que se actualiza)
    pygame.display.update()
    
#Salir
pygame.quit()