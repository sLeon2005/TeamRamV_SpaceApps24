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

bg = pygame.image.load("images\intro.jpeg")
bg = pygame.transform.scale(bg, DIMENSIONES)

while True:
    pantalla.blit(bg, (0,0))
    pygame.display.update()
    sleep(1)