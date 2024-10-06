import pygame

class Boton:
    def __init__(self, x, y, imagen_inicial, accion):
        self.imagen_inicial = imagen_inicial
        self.imagen = self.imagen_inicial  # Empieza con la imagen inicial
        self.rect = self.imagen.get_rect(topleft=(x, y))  # Definir la posición del botón
        self.accion = accion

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect)  # Dibuja el botón en la pantalla.

    def verificar_click(self, pos):
        if self.rect.collidepoint(pos):  # Solo ejecuta la acción si el clic está dentro del botón.
            self.accion()  # Ejecuta la acción asociada al botón

def cambiar_a_panel_siguiente(indice_actual, fondos):
    """
    Cambia al siguiente fondo de la lista de fondos.
    :param indice_actual: Índice del fondo actual.
    :param fondos: Lista de fondos disponibles.
    :return: Nuevo índice del fondo.
    """
    if indice_actual < len(fondos) - 1:
        return indice_actual + 1  # Pasar al siguiente fondo
    else:
        return 0  # Regresar al primero si ya está en el último

def cambiar_fondo(indice_fondo_actual, total_fondos, mostrar_boton_11=False):
    """Cambia el fondo actual y gestiona los botones."""
    if indice_fondo_actual < len(total_fondos) - 1:
        indice_fondo_actual += 1
    else:
        indice_fondo_actual = 0  # Reiniciar si se llega al último panel
    
    # Devolver si se muestra el botón y el índice del fondo actual
    return indice_fondo_actual, mostrar_boton_11

# Función específica para el botón en el panel 11
def cambiar_a_panel_12():
    """Cambia directamente al panel 12 desde el panel 11."""
    return 12
