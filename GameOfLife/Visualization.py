
from tkinter import *
from GameOfLife import Data


class Visualization:

    termination = False
    root = Tk()
    window = None
    grid = None

    def __init__(self, data):
        self.grid = data
        self.root.wm_title("Game of Life")
        self.window = Canvas(self.root, width=1200, height=1020)
        self.window.pack()
        self.initial_paint()
        self.paint()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.update()

    def update_visualization(self):
        self.root.update()

    def initial_paint(self):

        canvas = self.window

        canvas.create_rectangle(0, 0, 1200, 1020, fill='black')

        canvas.create_text(1100, 50, fill='light grey', font= "ubuntu 16", text='Generation: 0')

        i = 0
        while i < 51:
            canvas.create_line(10 + i * 20 , 10, 10 + i * 20, 1011, width=1, fill='grey')
            i = i + 1

        i = 0
        while i < 51:
            canvas.create_line(10,10 + i * 20 , 1011,10 + i * 20, width=1, fill='grey')
            i = i + 1


    def paint(self):

        canvas = self.window

        canvas.create_rectangle(1020, 0, 1200, 200, fill='black')


        canvas.create_text(1100, 50, fill='light grey', font="ubuntu 16", text='Generation: ' + str(self.grid.generation_number))

        for i in range(self.grid.get_grid_size()):
            for j in range(self.grid.get_grid_size()):
                if self.grid.get_Cell(i, j).get_state() == Data.State.ALIVE:
                    color = 'light grey'
                else:
                    color = 'black'

                canvas.create_rectangle(self.grid.get_Cell(i, j).get_top_left_x() + 1,
                                        self.grid.get_Cell(i, j).get_top_left_y() + 1,
                                        self.grid.get_Cell(i, j).get_top_left_x() + 19,
                                        self.grid.get_Cell(i, j).get_top_left_y() + 19,
                                        width=1, fill=color)

        self.root.update()

    def on_close(self):
        self.termination = True
        self.root.destroy()

    def window_state(self):
        return self.termination








