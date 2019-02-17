import tkinter as tk
from gui import GUI
from chess import Chess
from singleton import Singleton


def main():
    s = Singleton()
    chess = s.chess

    root = tk.Tk()
    root.title("Chess")
    gui = GUI(root, chess)
    gui.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
