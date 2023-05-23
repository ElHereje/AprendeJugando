'''
En este video vamos a poner dos texto en cada lado de la pantalla
donde se indiquen los puntos y las vueltas dadas.
Se va a usar otra fuente
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

fuente1 = pygame.font.SysFont("arial black", 33)

#definimos una 2ª fuente
fuente2 = pygame.font.SysFont("consolas", 24)


texto = fuente1.render("CUADRADOS", True, BLANCO)

#Datos
puntos = 0
vueltas = 0
r_x = 100
r_y = 300

#Bucle ppal
jugando = True
while jugando:
    
    #Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
        #Como prueba, cada vez que pulsemos "p", se suma 1 pto
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                puntos += 1
                
    
    #lógica
    r_x += 1
    if r_x > ANCHO:
        r_x = -100
        vueltas += 1

    # colocamos los dos textos dento del bucle porque van a ir cambiando
    texto_puntos = fuente2.render(f"Puntos: {str(puntos)}", True, BLANCO)
    texto_vueltas = fuente2.render(f"Puntos: {str(vueltas)}", True, BLANCO)
    
    #Dibujos:
    ventana.fill(NEGRO)
    #colocamos los textos:
    ventana.blit(texto, (260, 20))
    ventana.blit(texto_puntos, (30, 20))
    ventana.blit(texto_vueltas, (640, 20))
    pygame.draw.rect(ventana, VERDE, (r_x, r_y, 100, 100))
    
    #Actualizar (no se refleja nada hasta que se actualiza)
    pygame.display.update()
    pygame.time.delay(5)
    
#Salir
pygame.quit()