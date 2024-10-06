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

# ícono del juego
game_icon = pygame.image.load('images\icon.png')
pygame.display.set_icon(game_icon)

# Cargar las imágenes de fondo
fondos = cargar_fondos()

# Variables para controlar la visibilidad del botón
mostrar_boton = True
indice_fondo_actual = 0

# Cargar las imágenes del botón
imagen_boton_inicial = pygame.image.load("images/start.png").convert_alpha()
imagen_boton_11 = pygame.image.load("images/yes.png").convert_alpha()
imagen_boton_back = pygame.image.load("images/back.png").convert_alpha()
imagen_boton_back28 = pygame.image.load("images/back28.png").convert_alpha()
imagen_boton_tryagain = pygame.image.load("images/tryagain.png").convert_alpha()

imagen_boton_1 = pygame.image.load("images/1.png").convert_alpha()  # Botón para el panel 21
imagen_boton_2 = pygame.image.load("images/2.png").convert_alpha()
imagen_boton_3 = pygame.image.load("images/3.png").convert_alpha()

imagen_estrella_blanca = pygame.image.load("images/estrella_bl.png").convert_alpha()
imagen_estrella_azul = pygame.image.load("images/estrella_azul.png").convert_alpha()
imagen_estrella_azul2 = pygame.image.load("images/estrella_azul2.png").convert_alpha()
imagen_estrella_amarilla = pygame.image.load("images/estrella_amarilla.png").convert_alpha()
imagen_estrella_amarilla2 = pygame.image.load("images/estrella_amarilla2.png").convert_alpha()

imagen_estrella36_blanca = pygame.image.load("images/estrella36_blanca.png").convert_alpha()
imagen_estrella36_azul = pygame.image.load("images/estrella36_azul.png").convert_alpha()
imagen_estrella36_amarilla = pygame.image.load("images/estrella36_amarilla.png").convert_alpha()

imagen_boton_done234 = pygame.image.load("images/done.png").convert_alpha()
imagen_boton_done28 = pygame.image.load("images/done28.png").convert_alpha()

imagen_boton_1and2 = pygame.image.load("images/1and2.png")
imagen_boton_2and3 = pygame.image.load("images/2and3.png")


# Crear el botón inicial y asignar la función cambiar_fondo
boton_start = Boton(70, 310, imagen_boton_inicial, lambda: cambiar_fondo_local(1))

# Función para cambiar el fondo de manera local y ocultar el botón
def cambiar_fondo_local(siguiente_fondo):
    global indice_fondo_actual, mostrar_boton
    # print(f"Cambiando fondo a: {siguiente_fondo}")  # Debug
    indice_fondo_actual = siguiente_fondo  # Cambia al siguiente fondo
    mostrar_boton = False  # Ocultar el botón inicial al cambiar de panel




# Crear el botón del panel 11
boton_yes = Boton(200, 280, imagen_boton_11, lambda: cambiar_fondo_local(12))

# Crear el botón de retroceso
boton_back = Boton(39, 475, imagen_boton_back, lambda: cambiar_fondo_local(14))
boton_back28 = Boton(39, 475, imagen_boton_back28, lambda: cambiar_fondo_local(28))
boton_back36 = Boton(39, 475, imagen_boton_back28, lambda: cambiar_fondo_local(36))

boton_estrella_blanca = Boton(27,130, imagen_estrella_blanca, lambda: cambiar_fondo_local(16))
boton_estrella_azul = Boton(151,233, imagen_estrella_azul, lambda: cambiar_fondo_local(18))
boton_estrella_azul2 = Boton(278,316, imagen_estrella_azul2, lambda: cambiar_fondo_local(19))
boton_estrella_amarilla = Boton(258, 112, imagen_estrella_amarilla, lambda: cambiar_fondo_local(17))
boton_estrella_amarilla2 = Boton(28,349, imagen_estrella_amarilla2, lambda: cambiar_fondo_local(20))

boton_estrella28_blanca = Boton(20,180, imagen_estrella_blanca, lambda: cambiar_fondo_local(29))
boton_estrella28_azul = Boton(137,290, imagen_estrella_azul, lambda: cambiar_fondo_local(31))
boton_estrella28_amarilla = Boton(225, 120, imagen_estrella_amarilla, lambda: cambiar_fondo_local(30))

boton_estrella36_blanca = Boton(20,180, imagen_estrella36_blanca, lambda: cambiar_fondo_local(39))
boton_estrella36_azul = Boton(137,290, imagen_estrella36_azul, lambda: cambiar_fondo_local(38))
boton_estrella36_amarilla = Boton(225, 120, imagen_estrella36_amarilla, lambda: cambiar_fondo_local(37))

boton_done234 = Boton(10,600, imagen_boton_done234, lambda: cambiar_fondo_local(21))
boton_done28 = Boton(20, 500,imagen_boton_done28, lambda: cambiar_fondo_local(32))
boton_done36 = Boton(20, 500,imagen_boton_done28, lambda: cambiar_fondo_local(40))

boton_1and2 = Boton(75, 25, imagen_boton_1and2, lambda: cambiar_fondo_local(33))
boton_2and3 = Boton(75, 105, imagen_boton_2and3, lambda: cambiar_fondo_local(34))

boton_1and2_40 = Boton(75, 25, imagen_boton_1and2, lambda: cambiar_fondo_local(41))
boton_2and3_40 = Boton(75, 105, imagen_boton_2and3, lambda: cambiar_fondo_local(42))

# Crear los botones para el panel 21
boton_resultado_1 = Boton(175, 115, imagen_boton_1, lambda: cambiar_fondo_local(24))  # Botón que lleva al fondo 24
boton_resultado_2 = Boton(30, 190, imagen_boton_2, lambda: cambiar_fondo_local(22))  # Botón que lleva al fondo 22
boton_resultado_3 = Boton(176, 265, imagen_boton_3, lambda: cambiar_fondo_local(23))  # Botón que lleva al fondo 23

boton_tryagain = Boton(101, 33, imagen_boton_tryagain, lambda: cambiar_fondo_local(14))
boton_tryagain34 = Boton(95, 650, imagen_boton_tryagain, lambda: cambiar_fondo_local(28))
boton_tryagain40 = Boton(95, 650, imagen_boton_tryagain, lambda: cambiar_fondo_local(36))

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Verificar clic en el ratón
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                # print("Clic detectado en:", evento.pos)  # Log de clics
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
                        elif boton_done234.verificar_click(evento.pos):
                            print("Boton done clickeado")
                    elif indice_fondo_actual == 21:
                        # Verificar cada botón en orden
                        if boton_resultado_1.verificar_click(evento.pos):
                            print("Botón 1 clickeado (hacia panel 24)")  # Debug
                        elif boton_resultado_2.verificar_click(evento.pos):
                            print("Botón 2 clickeado (hacia panel 22)")  # Debug
                        elif boton_resultado_3.verificar_click(evento.pos):
                            print("Botón 3 clickeado (hacia panel 23)")  # Debug
                    elif indice_fondo_actual in (22,23,24):
                        if not boton_tryagain.rect.collidepoint(evento.pos):
                            print("Boton Try Again clickeado")
                            cambiar_fondo_local(25)
                        else:
                            boton_tryagain.verificar_click(evento.pos)
                            
                    elif indice_fondo_actual == 28:
                        boton_estrella28_blanca.verificar_click(evento.pos)
                        boton_estrella28_azul.verificar_click(evento.pos)
                        boton_estrella28_amarilla.verificar_click(evento.pos)
                        boton_done28.verificar_click(evento.pos)
                        
                    elif indice_fondo_actual in (29,30,31):
                        boton_back28.verificar_click(evento.pos)  

                    elif indice_fondo_actual == 32:
                        boton_1and2.verificar_click(evento.pos)
                        boton_2and3.verificar_click(evento.pos)    

                    elif indice_fondo_actual in (33,34):
                        if not boton_tryagain34.rect.collidepoint(evento.pos):
                            cambiar_fondo_local(35)
                        else:
                            boton_tryagain34.verificar_click(evento.pos)
                            
                    elif indice_fondo_actual == 36:
                        boton_estrella36_blanca.verificar_click(evento.pos)
                        boton_estrella36_azul.verificar_click(evento.pos)
                        boton_estrella36_amarilla.verificar_click(evento.pos)
                        boton_done36.verificar_click(evento.pos)
                        
                    elif indice_fondo_actual in(37,38,39):
                        boton_back36.verificar_click(evento.pos)
                        
                    elif indice_fondo_actual == 40:
                        boton_1and2_40.verificar_click(evento.pos)
                        boton_2and3_40.verificar_click(evento.pos)

                    elif indice_fondo_actual in (41,42):
                        if not boton_tryagain40.rect.collidepoint(evento.pos):
                            cambiar_fondo_local(43)
                        else:
                            boton_tryagain40.verificar_click(evento.pos)

                    # Verificar si estamos en paneles 15 a 20
                    elif 15 <= indice_fondo_actual <= 20:
                        boton_back.verificar_click(evento.pos)
                    elif indice_fondo_actual == 14 and not boton_back.rect.collidepoint(evento.pos):
                        cambiar_fondo_local(15)  # Avanzar al panel 15
                    elif indice_fondo_actual in (22, 23, 24):  # En paneles 22, 23, o 24
                        cambiar_fondo_local(25)  # Cambiar al panel 25
                    else:
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
        boton_done234.dibujar(pantalla)

    # Dibujar los botones del panel 21 si estamos en el panel 21
    if indice_fondo_actual == 21:
        boton_resultado_1.dibujar(pantalla)
        boton_resultado_2.dibujar(pantalla)
        boton_resultado_3.dibujar(pantalla)
        
    if indice_fondo_actual in (22,23,24):
        boton_tryagain.dibujar(pantalla)

    if indice_fondo_actual == 28:
        boton_estrella28_blanca.dibujar(pantalla)
        boton_estrella28_azul.dibujar(pantalla)
        boton_estrella28_amarilla.dibujar(pantalla)
        boton_done28.dibujar(pantalla)

    if indice_fondo_actual in (29,30,31):
        boton_back28.dibujar(pantalla)

    if indice_fondo_actual == 32:
        boton_1and2.dibujar(pantalla)
        boton_2and3.dibujar(pantalla)
        
    if indice_fondo_actual in (33,34):
        boton_tryagain34.dibujar(pantalla)

    if indice_fondo_actual == 36:
        boton_estrella36_blanca.dibujar(pantalla)
        boton_estrella36_azul.dibujar(pantalla)
        boton_estrella36_amarilla.dibujar(pantalla)
        boton_done36.dibujar(pantalla)
        
    if indice_fondo_actual in(37,38,39):
        boton_back36.dibujar(pantalla)
        
    if indice_fondo_actual == 40:
        boton_1and2_40.dibujar(pantalla)
        boton_2and3_40.dibujar(pantalla)

    elif indice_fondo_actual in (41,42):
        boton_tryagain40.dibujar(pantalla)
        
    # Dibujar el botón de retroceso si estamos en los paneles 15 a 19
    if 15 <= indice_fondo_actual <= 19:
        boton_back.dibujar(pantalla)

    # Actualizar la pantalla
    pygame.display.update()
