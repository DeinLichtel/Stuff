
from random import randint
from GameOfLife import Data
from tkinter import  *




class PresetData(Data.Grid):

    presetMatrix = None
    gridSize = None


    def __init__(self, size):
        Data.Grid.__init__(size)


    #def main(self):






    def random_preset(self, chance_for_live_cell):
        if chance_for_live_cell < 0 or chance_for_live_cell > 100 or chance_for_live_cell % 1 != 0:
            raise ValueError

        for i in range(self.gridSize):
            for j in range(self.gridSize):

                chance = randint(1, 100)

                if chance <= chance_for_live_cell:
                    self.presetMatrix[i][j] = Data.State.ALIVE


    def returnPreset(self):
        return self.presetMatrix

class PresetVisualization:

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


        i = 0
        while i < 51:
            canvas.create_line(10 + i * 20, 10, 10 + i * 20, 1011, width=1, fill='grey')
            i = i + 1

        i = 0
        while i < 51:
            canvas.create_line(10, 10 + i * 20, 1011, 10 + i * 20, width=1, fill='grey')
            i = i + 1

    def paint(self):

        canvas = self.window

        canvas.create_rectangle(1020, 0, 1200, 200, fill='black')


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



