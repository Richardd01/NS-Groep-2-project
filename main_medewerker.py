import tkinter as tk
from view.start_window import StartWindow

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.state("zoomed")
        self._frame = None
        self.switchFrame(StartWindow)


    def switchFrame(self, frameClass):
        """Destroys current frame and replaces it with a new one."""
        newFrame = frameClass(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = newFrame
        self._frame.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()