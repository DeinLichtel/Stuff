

class State:

    DEAD = 0
    ALIVE = 1


class Grid:

    matrix = None
    gridSize = None
    generation = 0

    def __init__(self, size):

        if size < 0:
            raise ValueError

        self.gridSize = size

        self.matrix = [None] * self.gridSize

        for i in range(len(self.matrix)):
            self.matrix[i] = [Cell(state=State.DEAD, tLX=0, tLY=0)] * self.gridSize

        for i in range(self.gridSize):

            for j in range(self.gridSize):

                self.matrix[i][j].set_state(i%2)
                self.matrix[i][j].set_topLeftX(10 + i * 20)
                print(i)
                print(j)
                print(10 + j * 20)

                #todo error

                self.matrix[i][j].set_topLeftY(10 + j * 20)






        for i in range(len(self.matrix)):
            print(self.matrix[i])

    def get_grid_size(self):
        return self.gridSize

    def get_Cell(self, x, y):
        return self.matrix[x][y]







class Cell:

    state = None
    topLeftX = 0
    topLeftY = 0

    def __init__(self, state, tLX, tLY):
        if (state != State.DEAD and state != State.ALIVE) or tLY < 0 or tLX <0:
            raise ValueError

        self.state = state
        self.topLeftX = tLX
        self.topLeftY = tLY

    def set_state(self, state):
        if state != State.DEAD and state != State.ALIVE:
            raise ValueError
        else:
            self.state = state

    def get_state(self):
        return self.state

    def __repr__(self):
        return str(self.topLeftY)

    def set_topLeftX(self, n):
        self.topLeftX = n

    def set_topLeftY(self, n):
        self.topLeftY = n

    def get_topLeftX(self):
        return self.topLeftX

    def get_topLeftY(self):
        return self.topLeftY








