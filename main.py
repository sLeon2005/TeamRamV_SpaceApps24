import pygame
from time import sleep

# inicializar pygame
pygame.init()

# dimensiones de la ventana
ANCHO = 405
ALTO = 720
DIMENSIONES = (ANCHO, ALTO)
pantalla = pygame.display.set_mode(DIMENSIONES)

# título de pantalla
pygame.display.set_caption("Exoplanets for Beginners!")

intro_imagen = pygame.image.load("images\intro.jpeg")
intro_imagen = pygame.transform.scale(intro_imagen, DIMENSIONES)

start_imagen = pygame.image.load("images\start.png")

# start_imagen.

loop = True
while loop:
    # checar si se cerró la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    # poner imagen de fondo
    pantalla.blit(intro_imagen, (0,0))
    # poner botón de start
    pantalla.blit(start_imagen, ((ANCHO-start_imagen.get_width())/2,360))

    # while start_imagen.

    pygame.display.update()
