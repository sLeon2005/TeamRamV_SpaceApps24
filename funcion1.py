import pygame

class Boton:
    def __init__(self, x, y, imagen_inicial, accion):
        #
        #Constructor del botón.
        #:param x: Posición X del botón.
        #:param y: Posición Y del botón.
        #:param imagen_inicial: Imagen del botón en su estado inicial.
        #:param imagen_cambio: Imagen del botón cuando se ha hecho clic.
        #:param accion: Función o acción que se ejecuta cuando se hace clic en el botón.
        
        self.imagen_inicial = imagen_inicial
        self.imagen = self.imagen_inicial  # Empieza con la imagen inicial
        self.rect = self.imagen.get_rect(topleft=(x, y))  # Definir la posición del botón
        self.accion = accion

    def dibujar(self, pantalla):
        #"""
        #Dibuja el botón en la pantalla.
        #:param pantalla: La superficie en la que se dibuja el botón.
        #"""
        pantalla.blit(self.imagen, self.rect)  # Dibuja el botón en la pantalla.

    def verificar_click(self, pos):
        #"""
        #Verifica si se ha hecho clic dentro del botón y ejecuta la acción correspondiente.
        #:param pos: Posición del ratón en el momento del clic.
        #"""
        if self.rect.collidepoint(pos):  # Solo ejecuta la acción si el clic está dentro del botón.
            self.accion()  # Ejecuta la acción asociada al botón
