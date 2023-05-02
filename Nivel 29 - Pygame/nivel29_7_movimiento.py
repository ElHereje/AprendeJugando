
'''
Partimos de una ventana con un cuadrado, que es lo que se mueve

'''


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

# datos
pos_x = 100
pos_y = 100

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
                
    
    # Lógica
    pos_x += 1
    # hacemos que vuelva al ppio cuando salga
    if pos_x > ANCHO:
        pos_x = 0
    #Dibujos:
    # fondo...
    ventana.fill(NEGRO) 
    
    # formas...
    pygame.draw.rect(ventana, VERDE, (pos_x, pos_y, 50 , 50))
    
    
    #Actualizar (no se refleja nada hasta que se actualiza)
    pygame.display.update()
    
    # relentizamos
    pygame.time.delay(5)
    
#Salir
pygame.quit()