import pygame
from funciones import Boton, cambiar_fondo, cambiar_a_panel_12  # Importar la clase Boton y las nuevas funciones
from fondos import cargar_fondos  # Importar la función de carga de fondos

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
fondos = cargar_fondos()
indice_fondo_actual = 0

# Variables para controlar la visibilidad del botón
mostrar_boton = True

# Cargar las imágenes del botón
imagen_boton_inicial = pygame.image.load("images/start.png").convert_alpha()
imagen_boton_11 = pygame.image.load("images/yes.png").convert_alpha()

# Crear el botón inicial y asignar la función cambiar_fondo
boton_start = Boton(70, 310, imagen_boton_inicial, lambda: cambiar_fondo_local(1))

# Función para cambiar el fondo de manera local y ocultar el botón
def cambiar_fondo_local(siguiente_fondo):
    global indice_fondo_actual, mostrar_boton
    indice_fondo_actual = siguiente_fondo  # Cambia al siguiente fondo
    mostrar_boton = False  # Ocultar el botón inicial al cambiar de panel

# Crear el botón del panel 11
boton_yes = Boton(100, 420, imagen_boton_11, lambda: cambiar_fondo_local(cambiar_a_panel_12()))

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Verificar clic en el ratón
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                if mostrar_boton:
                    boton_start.verificar_click(evento.pos)
                else:
                    if indice_fondo_actual == 11:
                        # Si estamos en el panel 11, verificamos el clic del botón "yes"
                        boton_yes.verificar_click(evento.pos)
                    else:
                        # Avanzar de panel si no estamos en el panel 11
                        indice_fondo_actual, _ = cambiar_fondo(indice_fondo_actual, fondos)

    # Limpiar pantalla con el fondo actual
    pantalla.blit(fondos[indice_fondo_actual], (0, 0))

    # Dibujar el botón inicial si está visible
    if mostrar_boton:
        boton_start.dibujar(pantalla)

    # Dibujar el botón del panel 11 si estamos en el panel 11
    if indice_fondo_actual == 11:
        boton_yes.dibujar(pantalla)

    # Actualizar la pantalla
    pygame.display.update()