import tkinter as tk
from ui.app_tkinter import AppGaraje


def iniciar_app():

    ventana = tk.Tk()
    AppGaraje(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    iniciar_app()