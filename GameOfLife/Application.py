import time
from GameOfLife import Visualization as Visualization
from GameOfLife import Data as Data


class Application:

    window = None
    grid = None

    def __init__(self):

        self.grid = Data.Grid(50)
        self.grid.random_preset(10)
        self.window = Visualization.Visualization(data=self.grid)
        self.main()

    def main(self):

        while not self.window.window_state():
            self.grid.generation()
            self.window.paint()
            time.sleep(1)





if __name__ == '__main__':
    Application()
