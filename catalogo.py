import tkinter as tk
from client.gui_app import Frame, menu_barra


def main():
    root = tk.Tk()
    root.title('Catalogo de peliculas por Alex')
    root.iconbitmap('img/al_logo.ico')
    menu_barra(root)
    app = Frame(root=root)
    app.mainloop()


if __name__ == '__main__':
    main()