'''
Igual qu el anterior pero  un cuadrado hacia la izq. y otro 
en diagonal

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
pos_x_a = 750
pos_y_a = 100
pos_x_b= 0
pos_y_b = 0

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
    pos_x_a -= 1
    if pos_x_a < -50:
        pos_x_a = ANCHO
        
    pos_x_b += 1
    pos_y_b += 1
    if pos_x_b > ANCHO:
        pos_x_b = -50
    if pos_y_b > ALTO:
        pos_y_b = -50
    
    # hacemos que vuelva al ppio cuando salga
    
    
        
    
    #Dibujos:
    # fondo...
    ventana.fill(NEGRO) 
    
    # formas...
    pygame.draw.rect(ventana, VERDE, (pos_x_a, pos_y_a, 50 , 50))
    pygame.draw.rect(ventana, AZUL, (pos_x_b, pos_y_b, 50 , 50))
    
    
    #Actualizar (no se refleja nada hasta que se actualiza)
    pygame.display.update()
    
    # relentizamos
    pygame.time.delay(5)
    
#Salir
pygame.quit()