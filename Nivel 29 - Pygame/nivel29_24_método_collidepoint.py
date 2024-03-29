import pygame

# inicializamos
pygame.init()

# medidas
ANCHO = 1280
ALTO = 720

# Colores
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
CLARO = (200, 165, 120)
MARRON = (120, 60, 20)

# Mapas

mapa = [
    "XXXXXXXXXXXXXXXX",
    "XXXFXXXXXXXXXFXX",
    "X              X",
    "X XXXXXX XXXXX X",
    "X XXXFXX  FXXX X",
    "X XXX XX XXXXF X",
    "X              X",
    "XXXXXXFXXXXXXXXX",
    "XXXXXXXXXXXXXXXX"
    ]

# Funciones
def dibujar_muro(superficie, rectangulo):
    pygame.draw.rect(superficie, MARRON, rectangulo)

def dibujar_manzana(superficie,rectangulo):
    pygame.draw.rect(superficie, VERDE, rectangulo)

def dibujar_personaje(superficie, rectangulo):
    pygame.draw.rect(superficie, AZUL, rectangulo)

# definimos una función que construya el mapa
def construir_mapa(mapa):
    muros = []
    manzanas = []
    x = 0
    y = 0
    for fila in mapa:
        for baldosa in fila:
            if baldosa == "X":
                muros.append(pygame.Rect(x, y, 80, 80))
            if baldosa == "F":
                manzanas.append(pygame.Rect(x, y, 80, 80))
            x += 80 # desplazamos el siguiente objeto
        
        x = 0
        y += 80
    return muros, manzanas

def dibujar_mapa(superficie, muros, manzanas):
    for muro in muros:
        dibujar_muro(superficie, muro)
    for manzana in manzanas:
        dibujar_manzana(superficie, manzana)

# Ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()

# Datos

# sustituimos los 4 muros del video anterior por todos los muros
muros, manzanas = construir_mapa(mapa) # esto nos devuelve la lista "muros"

personaje = pygame.Rect(100, 400, 40, 40)

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


    for muro in muros:
        if personaje.colliderect(muro):
            personaje.x -= personaje_vel_x
            personaje.y -= personaje_vel_y

    for manzana in list(manzanas):
        if personaje.collidepoint(manzana.centerx, manzana.centery):
            manzanas.remove(manzana)
        
    # Dibujos
    ventana.fill(CLARO)

    # por último, lo insertamos en la ventana
    dibujar_mapa(ventana, muros, manzanas)

    dibujar_personaje(ventana, personaje)


    # Actualizar
    pygame.display.update()


# Salir
pygame.quit()