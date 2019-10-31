import tkinter as tk
from view.start_window import StartWindow
from app import App

if __name__ == "__main__":
    app = App(StartWindow)
    app.mainloop()