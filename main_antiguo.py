# import pygame
# from time import sleep
# from funcion1 import Boton
# import random

# # inicializar pygame
# pygame.init()

# # dimensiones de la ventana
# ANCHO = 405
# ALTO = 720
# DIMENSIONES = (ANCHO, ALTO)
# pantalla = pygame.display.set_mode(DIMENSIONES)

# # título de pantalla
# pygame.display.set_caption("Exoplanets for Beginners!")

# intro_imagen = pygame.image.load("images\intro.jpeg")
# intro_imagen = pygame.transform.scale(intro_imagen, DIMENSIONES)

# start_imagen = pygame.image.load("images\start.png")
# # start_rect = start_imagen.get_rect()
# # start_rect.topleft = (ANCHO // 2 - start_rect.width // 2, ALTO // 2 - start_rect.height // 2)
# # print(start_rect[0])

# def siguiente():
#     print("SIGUIENTE")
#     print(random.randint(0,100))

# boton_start = Boton(70, 250, start_imagen, siguiente)

# # start_rect = start_imagen.get_rect()
# # # start_rect.topleft = (ANCHO // 2 - start_rect.width // 2, ALTO // 2 - start_rect.height // 2)
# # print(start_rect.topleft()[0])

# loop = True
# while loop:
#     # checar si se cerró la ventana
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             loop = False
#         # Detección de clic
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if event.button == 1:  # Botón izquierdo del ratón
#                 boton_start.verificar_click(event.pos)
#             # if start_rect[0] < event.pos[0] < start_rect[2] and start_rect[]:
#             #     print("lollllllllllllllllll")

#             # Set the x, y postions of the mouse click
#             # x, y = event.pos
#             # if start_imagen.get_rect().collidepoint(x, y):
#             #     print('clicked on image')
#             # print(event.pos)

#     # poner imagen de fondo
#     pantalla.blit(intro_imagen, (0,0))
#     # poner botón de start
#     pantalla.blit(start_imagen, ((ANCHO-start_imagen.get_width())/2,360))

#     # while start_imagen.

#     pygame.display.update()
