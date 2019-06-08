import time
from GameOfLife import Visualization as v


class Application:

    window = None

    def __init__(self):
        self.window = v.Visualization(app=self)
        self.main()

    def main(self):
        while not self.window.window_state():
            self.window.update_visualization()
            time.sleep(0.5)
            
    def createGrid(self, size):
        print("Dummy")


if __name__ == '__main__':
    Application()
