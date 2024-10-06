import pygame

def cargar_fondos():
    # Dimensiones de la ventana
    ANCHO = 405
    ALTO = 720
    DIMENSIONES = (ANCHO, ALTO)

    # Cargar las imágenes de fondo
    try:
        fondos = []
        for i in range(26):  # Cambia el rango según el número total de paneles
            fondo = pygame.image.load(f"images/panel{i}.jpeg")
            fondo = pygame.transform.scale(fondo, DIMENSIONES)
            fondos.append(fondo)

        return fondos  # Retornar la lista de fondos

    except pygame.error as e:
        print(f"Error al cargar las imágenes de fondo: {e}")
        return [pygame.Surface(DIMENSIONES)]  # En caso de error, retornar un fondo vacío