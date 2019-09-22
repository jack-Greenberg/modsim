from streets.intersection import Intersection
# from streets.street import Street

class Grid(object):
    """
    width (int): Number of intersections on the x-axis
    height (int): Number of intersections on the y-axis
    p_enter (float): Probability that a car enters the grid
    p_exit (float): Probability that a car exits the grid
    street_length (int): Number of cars each street can hold

    intersections: {
        (x_coord, y_coord): Intersection((x, y), timing, light_state)
    }
    graph: {
        (Intersection1, Intersection2): (cars on primary axis, cars on secondary axis)
    }
    """
    def __init__(self, width, height, p_enter, p_exit):
        self.width = width
        self.height = height
        self.p_enter = p_enter
        self.p_exit = p_exit
        self.intersections = {}
        self.graph = {}

        for i in range(width):
            for j in range(height):
                self.intersections[(i, j)] = Intersection((i, j), 60, True)

        for i in self.intersections:
            x_coord = i[0]
            y_coord = i[1]

            intersection1 = self.intersections[(x_coord, y_coord)]

            try: # Attempting to create the x-axis connections between intersections
                intersection2 = self.intersections[(x_coord + 1, y_coord)]
                self.graph[(intersection1, intersection2)] = (0, 0)
            except KeyError:
                pass

            try: # Attempting to create the y-axis connections between intersections
                intersection3 = self.intersections[(x_coord, y_coord + 1)]
                self.graph[(intersection1, intersection3)] = (0, 0)
            except KeyError:
                pass

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
