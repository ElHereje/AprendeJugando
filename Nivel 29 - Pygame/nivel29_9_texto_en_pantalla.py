'''
Para colocar u texto:
1 - definimos una fuente.
2 - creamos un objeto de tipoi superficie.
3 - pegar la superficie en la ventana

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

#Ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))

# Definimos la fuente de texto:
fuente = pygame.font.SysFont("arial black", 33)

# ceamos una superficie donde escribir el texto (texto, suavizado, color)
texto = fuente.render("CUADRADOS", True, BLANCO)

#Datos
r_x = 100
r_y = 300

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
                
    
    #lógica
    r_x += 1
    if r_x > ANCHO:
        r_x = -100
    
    #Dibujos:
    ventana.fill(NEGRO)
    #colocamos el texto:
    ventana.blit(texto, (260, 20))
    pygame.draw.rect(ventana, VERDE, (r_x, r_y, 100, 100))
    
    #Actualizar (no se refleja nada hasta que se actualiza)
    pygame.display.update()
    pygame.time.delay(5)
    
#Salir
pygame.quit()