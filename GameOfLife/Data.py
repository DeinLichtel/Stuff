from random import randint

class State:

    DEAD = 0
    ALIVE = 1


class Grid:

    matrix = None
    gridSize = None
    generation_number = 0

    def __init__(self, size):

        if size < 0:
            raise ValueError

        self.gridSize = size

        self.matrix = [[Cell(state=State.DEAD, tlx=0, tly=0) for x in range(self.gridSize)] for y in range(self.gridSize)]

        for i in range(self.gridSize):

            for j in range(self.gridSize):


                self.matrix[i][j].set_top_left_x(10 + j * 20)
                self.matrix[i][j].set_top_left_y(10 + i * 20)


        #print data:
        #for i in range(len(self.matrix)):
        #    print(self.matrix[i])

    def get_grid_size(self):
        return self.gridSize

    def get_Cell(self, x, y):
        return self.matrix[x][y]

    def generation(self):

        temp_matrix = [[State.DEAD for x in range(self.gridSize)] for y in range(self.gridSize)]

        for i in range(self.gridSize):
            for j in range(self.gridSize):

                live_neighbours = self.count_live_neighbours(i, j)


                if self.matrix[i][j].get_state() == State.DEAD and live_neighbours == 3:
                    temp_matrix[i][j] = State.ALIVE


                if self.matrix[i][j].get_state() == State.ALIVE and live_neighbours >= 2 and live_neighbours <= 3:
                    temp_matrix[i][j] = State.ALIVE




        self.copy_states(temp_matrix)
        self.generation_number = self.generation_number + 1

    def copy_states(self, state_list):

        for i in range(self.gridSize):
            for j in range(self.gridSize):
                self.matrix[i][j].set_state(state_list[i][j])



    def count_live_neighbours(self, x, y):

        count = 0

        tlx = (x - 1 + self.gridSize) % self.gridSize
        tly = (y - 1 + self.gridSize) % self.gridSize



        for i in range(3):
            for j in range(3):
                if self.matrix[(tlx + i) % self.gridSize][(tly + j) % self.gridSize].get_state() == State.ALIVE:
                    count = count + 1

        if self.matrix[x][y].get_state() == State.ALIVE:
            return count - 1
        else:
            return count


    #moved to preset, still left here to retain functionality
    def random_preset(self, chance_for_live_cell):
        if chance_for_live_cell < 0 or chance_for_live_cell > 100 or chance_for_live_cell % 1 != 0:
            raise ValueError

        for i in range(self.gridSize):
            for j in range(self.gridSize):

                chance = randint(1, 100)

                if chance <= chance_for_live_cell:
                    self.matrix[i][j].set_state(State.ALIVE)




















class Cell:

    state = None
    top_left_x = 0
    top_left_y = 0

    def __init__(self, state, tlx, tly):
        if (state != State.DEAD and state != State.ALIVE) or tly < 0 or tlx <0:
            raise ValueError

        self.state = state
        self.top_left_x = tlx
        self.top_left_y = tly

    def set_state(self, state):
        if state != State.DEAD and state != State.ALIVE:
            raise ValueError
        else:
            self.state = state

    def get_state(self):
        return self.state

    def __repr__(self):
        return str(self.top_left_x)

    def set_top_left_x(self, n):
        self.top_left_x = n

    def set_top_left_y(self, n):
        self.top_left_y = n

    def get_top_left_x(self):
        return self.top_left_x

    def get_top_left_y(self):
        return self.top_left_y








