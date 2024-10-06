import pygame
from funciones import Boton, cambiar_a_panel_anterior
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
imagen_boton_1 = pygame.image.load("images/1.png").convert_alpha()  # Botón para el panel 21
imagen_boton_2 = pygame.image.load("images/2.png").convert_alpha()
imagen_boton_3 = pygame.image.load("images/3.png").convert_alpha()
imagen_estrella_blanca = pygame.image.load("images/estrella_bl.png").convert_alpha()
imagen_estrella_azul = pygame.image.load("images/estrella_azul.png").convert_alpha()
imagen_estrella_azul2 = pygame.image.load("images/estrella_azul2.png").convert_alpha()
imagen_estrella_amarilla = pygame.image.load("images/estrella_amarilla.png").convert_alpha()
imagen_estrella_amarilla2 = pygame.image.load("images/estrella_amarilla2.png").convert_alpha()
imagen_boton_done = pygame.image.load("images/done.png").convert_alpha()

# Crear el botón inicial y asignar la función cambiar_fondo
boton_start = Boton(70, 310, imagen_boton_inicial, lambda: cambiar_fondo_local(1))

# Función para cambiar el fondo de manera local y ocultar el botón
def cambiar_fondo_local(siguiente_fondo):
    global indice_fondo_actual, mostrar_boton
    print(f"Cambiando fondo a: {siguiente_fondo}")  # Debug
    indice_fondo_actual = siguiente_fondo  # Cambia al siguiente fondo
    mostrar_boton = False  # Ocultar el botón inicial al cambiar de panel

# Crear el botón del panel 11
boton_yes = Boton(200, 280, imagen_boton_11, lambda: cambiar_fondo_local(12))

# Crear el botón de retroceso
boton_back = Boton(39, 475, imagen_boton_back, lambda: cambiar_fondo_local(14))

boton_estrella_blanca = Boton(27,130, imagen_estrella_blanca, lambda: cambiar_fondo_local(16))
boton_estrella_azul = Boton(151,233, imagen_estrella_azul, lambda: cambiar_fondo_local(18))
boton_estrella_azul2 = Boton(278,316, imagen_estrella_azul2, lambda: cambiar_fondo_local(19))
boton_estrella_amarilla = Boton(258, 112, imagen_estrella_amarilla, lambda: cambiar_fondo_local(17))
boton_estrella_amarilla2 = Boton(28,349, imagen_estrella_amarilla2, lambda: cambiar_fondo_local(20))

boton_done = Boton(10,600, imagen_boton_done, lambda:cambiar_fondo_local(21))

# Crear los botones para el panel 21
boton_resultado_1 = Boton(175, 115, imagen_boton_1, lambda: cambiar_fondo_local(24))  # Botón que lleva al fondo 24
boton_resultado_2 = Boton(30, 190, imagen_boton_2, lambda: cambiar_fondo_local(22))  # Botón que lleva al fondo 22
boton_resultado_3 = Boton(176, 265, imagen_boton_3, lambda: cambiar_fondo_local(23))  # Botón que lleva al fondo 23

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
                            
                    elif indice_fondo_actual == 14:
                        # Verificar cada botón en orden
                        if boton_estrella_blanca.verificar_click(evento.pos):
                            print("Botón 1 clickeado (hacia panel 16)")  # Debug
                        elif boton_estrella_amarilla.verificar_click(evento.pos):
                            print("Botón 2 clickeado (hacia panel 17)")  # Debug
                        elif boton_estrella_azul.verificar_click(evento.pos):
                            print("Botón 3 clickeado (hacia panel 18)")  # Debug
                        elif boton_estrella_amarilla2.verificar_click(evento.pos):
                            print("Botón 2 clickeado (hacia panel 20)")  # Debug
                        elif boton_estrella_azul2.verificar_click(evento.pos):
                            print("Botón 3 clickeado (hacia panel 19)")  # Debug  
                        elif boton_done.verificar_click(evento.pos):
                            print("Boton done clickeado")
                            
                            
                    elif indice_fondo_actual == 21:
                        # Verificar cada botón en orden
                        if boton_resultado_1.verificar_click(evento.pos):
                            print("Botón 1 clickeado (hacia panel 24)")  # Debug
                        elif boton_resultado_2.verificar_click(evento.pos):
                            print("Botón 2 clickeado (hacia panel 22)")  # Debug
                        elif boton_resultado_3.verificar_click(evento.pos):
                            print("Botón 3 clickeado (hacia panel 23)")  # Debug
                            
                    
                            
                        # No es necesario cambiar de panel aquí, ya que lo hacemos al hacer clic en el botón
                    elif 15 <= indice_fondo_actual <= 20:  # Verificar si estamos en paneles 15 a 20
                        boton_back.verificar_click(evento.pos)
                    elif indice_fondo_actual == 14 and not boton_back.rect.collidepoint(evento.pos):
                        cambiar_fondo_local(15)  # Avanzar al panel 15
                    elif indice_fondo_actual in (22, 23, 24):  # En paneles 22, 23, o 24
                        cambiar_fondo_local(25)  # Cambiar al panel 25
                    else:
                        # Cambiar al siguiente panel automáticamente
                        cambiar_fondo_local(indice_fondo_actual + 1)

    # Limpiar pantalla con el fondo actual
    if 0 <= indice_fondo_actual < len(fondos):
        pantalla.blit(fondos[indice_fondo_actual], (0, 0))

    # Dibujar el botón inicial si está visible
    if mostrar_boton:
        boton_start.dibujar(pantalla)

    # Dibujar el botón del panel 11 si estamos en el panel 11
    if indice_fondo_actual == 11:
        boton_yes.dibujar(pantalla)

    if indice_fondo_actual == 14:
        boton_estrella_blanca.dibujar(pantalla)
        boton_estrella_amarilla.dibujar(pantalla)
        boton_estrella_azul.dibujar(pantalla)
        boton_estrella_amarilla2.dibujar(pantalla)
        boton_estrella_azul2.dibujar(pantalla)
        boton_done.dibujar(pantalla)

    # Dibujar los botones del panel 21 si estamos en el panel 21
    if indice_fondo_actual == 21:
        boton_resultado_1.dibujar(pantalla)
        boton_resultado_2.dibujar(pantalla)
        boton_resultado_3.dibujar(pantalla)
        

    # Dibujar el botón de retroceso si estamos en los paneles 15 a 19
    if 15 <= indice_fondo_actual <= 19:
        boton_back.dibujar(pantalla)

    # Actualizar la pantalla
    pygame.display.update()
