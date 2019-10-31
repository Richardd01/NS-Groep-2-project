import tkinter as tk
from app import App
from view.consumenten_window import ConsumentenWindow

if __name__ == "__main__":
    app = App(ConsumentenWindow)
    app.mainloop()