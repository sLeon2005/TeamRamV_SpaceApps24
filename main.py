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

while True:
    pantalla.blit(bg, (0,0))
    pygame.display.update()
    sleep(1)