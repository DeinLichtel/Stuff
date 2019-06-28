import time
from GameOfLife import Visualization as Visualization
from GameOfLife import Data as Data


class Application:

    window = None
    grid = None

    def __init__(self):

        self.grid = Data.Grid(50)
        self.grid.random_preset(30)
        self.window = Visualization.Visualization(data=self.grid)
        time.sleep(0.5)
        self.main()

    def main(self):

        while not self.window.window_state():
            self.grid.generation()
            self.window.paint()
            time.sleep(0.5)





if __name__ == '__main__':
    Application()
