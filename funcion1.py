import tkinter as tk
from tkinter import PhotoImage

def crear_boton(ventana):
    button_image = PhotoImage(file="ruta/a/tu_imagen.png")
    start_button = tk.Button(ventana, image=button_image, command=start_game)
    start_button.image = button_image  # Mantener referencia a la imagen
    start_button.pack(pady=20)
    
    def start_game():
        print("juega bru")