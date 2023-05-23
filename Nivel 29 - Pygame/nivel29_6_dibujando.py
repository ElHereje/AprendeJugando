'''dibujar un cuadro de 100 x 100 en cada esquina, con distancia
de los bordes de 10px, un círculo en el centro, lineas y un poligono
irregular'''

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
    
    # rectangulos --> lugar, color, (x, y, ancho, alto)
    pygame.draw.rect(ventana, VERDE, (10, 10, 100, 100))
    pygame.draw.rect(ventana, AZUL, (690, 10, 100, 100))
    pygame.draw.rect(ventana, ROJO, (10, 490, 100, 100))
    pygame.draw.rect(ventana, BLANCO, (690, 490, 100, 100))
    # circulo en el centro --> lugar, color, centro, radio
    pygame.draw.circle(ventana, VERDE, (400, 300), 50)
    
    # lineas --> lugar, color, origen, final
    pygame.draw.line(ventana, BLANCO, (200, 300), (300, 500))
    
    # figuras irregulares
    pygame.draw.polygon(ventana, BLANCO, ((300, 300), (350, 300),
                                          (350, 250), (400, 250),
                                          (400, 300), (450, 300),
                                          (450, 350), (300, 350)
                                          ))
    
    #Actualizar (no se refleja nada hasta que se actualiza)
    pygame.display.update()
    
#Salir
pygame.quit()