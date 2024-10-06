import pygame
from funciones import Boton, cambiar_fondo, cambiar_a_panel_anterior
from fondos import cargar_fondos

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

# Variables para controlar la visibilidad del botón
mostrar_boton = True
indice_fondo_actual = 0

# Cargar las imágenes del botón
imagen_boton_inicial = pygame.image.load("images/start.png").convert_alpha()
imagen_boton_11 = pygame.image.load("images/yes.png").convert_alpha()
imagen_boton_back = pygame.image.load("images/back.png").convert_alpha()

# Crear el botón inicial y asignar la función cambiar_fondo
boton_start = Boton(70, 310, imagen_boton_inicial, lambda: cambiar_fondo_local(1))

# Función para cambiar el fondo de manera local y ocultar el botón
def cambiar_fondo_local(siguiente_fondo):
    global indice_fondo_actual, mostrar_boton
    indice_fondo_actual = siguiente_fondo  # Cambia al siguiente fondo
    mostrar_boton = False  # Ocultar el botón inicial al cambiar de panel

# Crear el botón del panel 11
boton_yes = Boton(200, 280, imagen_boton_11, lambda: cambiar_fondo_local(12))

# Crear el botón de retroceso
boton_back = Boton(39, 475, imagen_boton_back, lambda: cambiar_fondo_local(cambiar_a_panel_anterior(indice_fondo_actual)))

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Verificar clic en el ratón
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                print("Clic detectado en:", evento.pos)  # Log de clics
                if mostrar_boton:
                    boton_start.verificar_click(evento.pos)
                else:
                    if indice_fondo_actual == 11:
                        boton_yes.verificar_click(evento.pos)
                    elif 15 <= indice_fondo_actual <= 19:  # Verificar si estamos en paneles 15 a 19
                        boton_back.verificar_click(evento.pos)
                    elif indice_fondo_actual == 14 and not boton_back.rect.collidepoint(evento.pos):
                        cambiar_fondo_local(15)  # Avanzar al panel 15
                    else:
                        # Cambiar al siguiente panel automáticamente
                        cambiar_fondo_local(indice_fondo_actual + 1)

            # Manejo de clics en paneles específicos
            if indice_fondo_actual == 15 and not boton_back.rect.collidepoint(evento.pos):  # Si no se hizo clic en "back"
                cambiar_fondo_local(16)  # Avanzar al panel 16
            elif indice_fondo_actual == 16 and not boton_back.rect.collidepoint(evento.pos):  # Si no se hizo clic en "back"
                cambiar_fondo_local(17)  # Avanzar al panel 17
            elif indice_fondo_actual == 17 and not boton_back.rect.collidepoint(evento.pos):  # Si no se hizo clic en "back"
                cambiar_fondo_local(18)  # Avanzar al panel 18
            elif indice_fondo_actual == 18 and not boton_back.rect.collidepoint(evento.pos):  # Si no se hizo clic en "back"
                cambiar_fondo_local(19)  # Avanzar al panel 19
            elif indice_fondo_actual == 19 and not boton_back.rect.collidepoint(evento.pos):  # Si no se hizo clic en "back"
                cambiar_fondo_local(20)  # Avanzar al panel 19
            elif indice_fondo_actual == 20 and not boton_back.rect.collidepoint(evento.pos):  # Si no se hizo clic en "back"
                cambiar_fondo_local(0)  # Volver al panel 0 (o al que prefieras)

    # Limpiar pantalla con el fondo actual
    if 0 <= indice_fondo_actual < len(fondos):
        pantalla.blit(fondos[indice_fondo_actual], (0, 0))

    # Dibujar el botón inicial si está visible
    if mostrar_boton:
        boton_start.dibujar(pantalla)

    # Dibujar el botón del panel 11 si estamos en el panel 11
    if indice_fondo_actual == 11:
        boton_yes.dibujar(pantalla)

    # Dibujar el botón de retroceso si estamos en los paneles 15 a 19
    if 15 <= indice_fondo_actual <= 19:
        boton_back.dibujar(pantalla)

    # Actualizar la pantalla
    pygame.display.update()