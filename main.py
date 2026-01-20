import tkinter as tk
from utils.gestorVentanas import GestorVentanas
from pantallas.bienvenida import PantallaBienvenida

def main():
    root = tk.Tk()
    root.title("BizaScanner")
    root.state('zoomed')

    gestor = GestorVentanas(root)
    gestor.cambiar_pantalla(PantallaBienvenida)

    root.mainloop()

if __name__ == "__main__":
    main()