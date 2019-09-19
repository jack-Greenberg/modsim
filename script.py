from streets.intersection import Intersection
# from streets.street import Street

class Grid(object):
    """
    width (int): Number of intersections on the x-axis
    height (int): Number of intersections on the y-axis
    p_enter (float): Probability that a car enters the grid
    p_exit (float): Probability that a car exits the grid
    """
    def __init__(self, width, height, p_enter, p_exit):
        self.width = width
        self.height = height
        self.p_enter = p_enter
        self.p_exit = p_exit
        self.intersections = []

        for i in range(width):
            for j in range(height):
                self.intersections.append(Intersection((i, j), 60, True))

    def __str__(self):
        string = []
        for _ in range(self.width):
            string += "  |"
        string += "\n"

        for _ in range(self.height):
            for _ in range (self.width):
                string += "--+"
            string += "--"
            string += "\n"
            for _ in range(self.width):
                string += "  |"
            string += "\n"
        return "".join(string)
    
    def step(self):
        for i in self.intersections:
            if (i.position[0] in [0, self.width - 1]) or (i.position[1] in [0, self.height - 1]):
                pass
        return self.intersections

grid = Grid(4,3, .1, .2)
print(grid)
# print(grid.step())
