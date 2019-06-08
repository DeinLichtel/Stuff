import time
from GameOfLife import Visualization as Visualization
from GameOfLife import Data as Data


class Application:

    window = None
    grid = None

    def __init__(self):

        self.grid = Data.Grid(50)
        self.window = Visualization.Visualization(data=self.grid)
        self.main()

    def main(self):

        while not self.window.window_state():
            self.window.update_visualization()
            time.sleep(0.5)





if __name__ == '__main__':
    Application()
