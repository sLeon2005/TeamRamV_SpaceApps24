import pygame
from funcion1 import Boton  # Importar la clase Boton

# Inicializar pygame
pygame.init()

# Dimensiones de la ventana
ANCHO = 405
ALTO = 720
DIMENSIONES = (ANCHO, ALTO)
pantalla = pygame.display.set_mode(DIMENSIONES)

# Título de pantalla
pygame.display.set_caption("Exoplanets for Beginners!")

# Cargar las imágenes de fondo
bg_1 = pygame.image.load("images/intro.jpeg")
bg_1 = pygame.transform.scale(bg_1, DIMENSIONES)

bg_2 = pygame.image.load("images/panel1.jpeg")  # La nueva imagen de fondo
bg_2 = pygame.transform.scale(bg_2, DIMENSIONES)

bg_3 = pygame.image.load("images/panel2.jpeg")  # Otro panel para después de hacer clic en la pantalla
bg_3 = pygame.transform.scale(bg_3, DIMENSIONES)

# Variables para controlar el estado del fondo y la visibilidad del botón
fondo_actual = bg_1
mostrar_boton = True
fondo_cambiado = False  # Para controlar si el fondo ya ha cambiado

# Cargar las imágenes del botón
imagen_boton_inicial = pygame.image.load("images/start.png").convert_alpha()

# Función para cambiar la imagen de fondo y quitar el botón
def cambiar_fondo():
    global fondo_actual, mostrar_boton, fondo_cambiado
    fondo_actual = bg_2  # Cambia al segundo fondo
    mostrar_boton = False  # Quita el botón después de hacer clic
    fondo_cambiado = True  # Marcar que el fondo ha cambiado

# Crear el botón y asignar la función cambiar_fondo como acción
boton_start = Boton(70, 310, imagen_boton_inicial, cambiar_fondo)

# Función para pasar al siguiente panel
def cambiar_a_panel_siguiente():
    global fondo_actual
    fondo_actual = bg_3  # Cambiar al tercer panel

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Verificar clic en el ratón
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Botón izquierdo del ratón
                if mostrar_boton:  # Verificar el clic en el botón si está visible
                    boton_start.verificar_click(evento.pos)
                elif fondo_cambiado:  # Si ya se cambió el fondo, cualquier clic cambia al panel siguiente
                    cambiar_a_panel_siguiente()

    # Limpiar pantalla con la imagen de fondo actual
   
