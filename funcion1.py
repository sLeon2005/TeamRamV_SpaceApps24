import pygame

class Boton:
    def __init__(self, x, y, imagen, accion):
        self.imagen = imagen
        self.rect = self.imagen.get_rect(topleft=(x, y))
        self.accion = accion

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect)

    def verificar_click(self, pos):
        if self.rect.collidepoint(pos):
            self.accion()