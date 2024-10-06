# fondos.py
import pygame

def cargar_fondos():
    
    # Dimensiones de la ventana
    ANCHO = 405
    ALTO = 720
    DIMENSIONES = (ANCHO, ALTO)

    # Cargar las imágenes de fondo
    try:
        bg_0 = pygame.image.load("images/intro.jpeg")
        bg_0 = pygame.transform.scale(bg_0, DIMENSIONES)

        bg_1 = pygame.image.load("images/panel1.jpeg")
        bg_1 = pygame.transform.scale(bg_1, DIMENSIONES)

        bg_2 = pygame.image.load("images/panel2.jpeg")
        bg_2 = pygame.transform.scale(bg_2, DIMENSIONES)

        bg_3 = pygame.image.load("images/panel3.jpeg")
        bg_3 = pygame.transform.scale(bg_3, DIMENSIONES)

        bg_4 = pygame.image.load("images/panel4.jpeg")
        bg_4 = pygame.transform.scale(bg_4, DIMENSIONES)

        bg_5 = pygame.image.load("images/panel5.jpeg")
        bg_5 = pygame.transform.scale(bg_5, DIMENSIONES)

        bg_6 = pygame.image.load("images/panel6.jpeg")
        bg_6 = pygame.transform.scale(bg_6, DIMENSIONES)

        bg_7 = pygame.image.load("images/panel7.jpeg")
        bg_7 = pygame.transform.scale(bg_7, DIMENSIONES)

        bg_8 = pygame.image.load("images/panel8.jpeg")
        bg_8 = pygame.transform.scale(bg_8, DIMENSIONES)
        
        bg_9 = pygame.image.load("images/panel9.jpeg")
        bg_9 = pygame.transform.scale(bg_9, DIMENSIONES)
        
        bg_10 = pygame.image.load("images/panel10.jpeg")
        bg_10 = pygame.transform.scale(bg_10, DIMENSIONES)
        
        bg_11 = pygame.image.load("images/panel11.jpeg")
        bg_11 = pygame.transform.scale(bg_11, DIMENSIONES)
        

        return [bg_0, bg_1, bg_2, bg_3, bg_4, bg_5, bg_6, bg_7, bg_8, bg_9, bg_10, bg_11]

    except pygame.error as e:
        print(f"Error al cargar las imágenes de fondo: {e}")
        return [pygame.Surface(DIMENSIONES)]  # Retornar un fondo negro en caso de error
