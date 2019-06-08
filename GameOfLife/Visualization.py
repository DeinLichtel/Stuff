
from tkinter import *


class Visualization:

    termination = False
    root = Tk()
    application = None

    def __init__(self, app):
        self.application = app
        self.root.title = "Game of Life"
        window = Canvas(self.root, width=1000, height=1000)
        window.pack()
        self.paint(canvas=window)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.update()

    def update_visualization(self):
        self.root.update()

    def paint(self, canvas):

        canvas.create_line(10, 10, 20, 20)

        self.root.update()

    def on_close(self):
        self.termination = True
        self.root.destroy()

    def window_state(self):
        return self.termination








