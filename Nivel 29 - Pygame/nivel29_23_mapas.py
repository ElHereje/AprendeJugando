'''
Vamos a ver una forma mas eficiente de colocar muros para un programa
con múltiples habitaciones.....

hay que calcular el nº de baldosas según las medidas:
para baldosas de 80x80:
1280 / 80 = 16 baldosas a lo largo
720 / 80 = 9 baldosas


'''

import pygame

# Inicializar
pygame.init()

# Medidas
ANCHO = 1280
ALTO = 720

# Colores
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
MARRON = (150, 70, 10)

# DEFINIMOS LOS MAPAS (16 columnas y 9 filas)
mapa = [
    "XXXXXXXXXXXXXXXX",
    "X              X",
    "X XXXXXX XXXXX X",
    "X X            X",
    "X XXXX XXXXXXX X",
    "X X    X       X",
    "X XX XXXXX XXX X",
    "X              X",
    "XXXXXXXXXXXXXXXX"
    ]

# Funciones
def dibujar_muro(superficie, rectangulo):
    pygame.draw.rect(superficie, MARRON, rectangulo)

def dibujar_personaje(superficie, rectangulo):
    pygame.draw.rect(superficie, AZUL, rectangulo)

# definimos una función que construya el mapa
def construir_mapa(mapa):
    muros = []
    x = 0
    y = 0
    for fila in mapa:
        for muro in fila:
            if muro == "X":
                muros.append(pygame.Rect(x, y, 80, 80))
            x += 80 # desplazamos el siguiente objeto
        
        x = 0
        y += 80
    return muros

# una vez construido, hay que dibujarlo
def dibujar_mapa(superficie, muros):
    for muro in muros:
        dibujar_muro(superficie, muro)


# Ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()

# Datos

# sustituimos los 4 muros del video anterior por todos los muros
muros = construir_mapa(mapa) # esto nos devuelve la lista "muros"

personaje = pygame.Rect(100, 100, 40, 40)

personaje_vel_x = 0
personaje_vel_y = 0


# Bucle principal
jugando = True
while jugando:

    reloj.tick(60)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                jugando = False
            if event.key == pygame.K_RIGHT:
                personaje_vel_x = 10
            if event.key == pygame.K_LEFT:
                personaje_vel_x = -10
            if event.key == pygame.K_DOWN:
                personaje_vel_y = 10
            if event.key == pygame.K_UP:
                personaje_vel_y = -10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                personaje_vel_x = 0
            if event.key == pygame.K_LEFT:
                personaje_vel_x = 0
            if event.key == pygame.K_DOWN:
                personaje_vel_y = 0
            if event.key == pygame.K_UP:
                personaje_vel_y = 0        


    # Lógica
    personaje.x += personaje_vel_x
    personaje.y += personaje_vel_y

    if personaje.x > ANCHO - personaje.width:
        personaje.x = ANCHO - personaje.width
    if personaje.x < 0:
        personaje.x = 0
    if personaje.y > ALTO - personaje.height:
        personaje.y = ALTO - personaje.height
    if personaje.y < 0:
        personaje.y = 0

    for muro in muros:
        if personaje.colliderect(muro):
            personaje.x -= personaje_vel_x
            personaje.y -= personaje_vel_y
        
    # Dibujos
    ventana.fill(NEGRO)

    # por último, lo insertamos en la ventana
    dibujar_mapa(ventana, muros)

    dibujar_personaje(ventana, personaje)


    # Actualizar
    pygame.display.update()


# Salir
pygame.quit()