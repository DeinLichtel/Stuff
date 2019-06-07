class Application:

    gridSize = 0

    def __init__(self):
        print("Hello World")


    def main(self):
        value = input("Enter grid size.\n")
        try:
            global gridSize
            gridSize = int(value)
            print("Your input was " + str(gridSize))
        except ValueError:
            print("Invalid input!")
            return




    def createGrid(self, size):
        print("Dummy")















if __name__ == '__main__':
    x = Application()
    x.main()