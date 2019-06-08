
from tkinter import *
from GameOfLife import Data


class Visualization:

    termination = False
    root = Tk()
    grid = None

    def __init__(self, data):
        self.grid = data
        self.root.title = "Game of Life"
        window = Canvas(self.root, width=1200, height=1020)
        window.pack()
        self.initial_paint(canvas=window)
        self.paint(canvas=window)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.update()

    def update_visualization(self):
        self.root.update()

    def initial_paint(self, canvas):

        canvas.create_rectangle(0, 0, 1200, 1020, fill='black')

        i = 0
        while i < 51:
            canvas.create_line(10 + i * 20 , 10, 10 + i * 20, 1011, width=1, fill='grey')
            i = i + 1

        i = 0
        while i < 51:
            canvas.create_line(10,10 + i * 20 , 1011,10 + i * 20, width=1, fill='grey')
            i = i + 1

    def paint(self, canvas):

        for i in range(self.grid.get_grid_size()):
            for j in range(self.grid.get_grid_size()):
                if self.grid.get_Cell(i, j).get_state() == Data.State.ALIVE:
                    color = 'light grey'
                else:
                    color = 'black'

                canvas.create_rectangle(self.grid.get_Cell(i, j).get_topLeftX() + 1,
                                        self.grid.get_Cell(i, j).get_topLeftY() + 1,
                                        self.grid.get_Cell(i, j).get_topLeftX() + 19,
                                        self.grid.get_Cell(i, j).get_topLeftY() + 19,
                                        width=1, fill=color)

        self.root.update()

    def on_close(self):
        self.termination = True
        self.root.destroy()

    def window_state(self):
        return self.termination








