from streets.intersection import Intersection
import random
from datetime import datetime

class Grid(object):
    """
    width (int): Number of intersections on the x-axis
    height (int): Number of intersections on the y-axis
    p_enter (float): Probability that a car enters the grid
    p_exit (float): Probability that a car exits the grid
    street_length (int): Number of cars each street can hold

    intersections: {
        (x_coord, y_coord): Intersection((x, y), timing, light_state),
        ...
    }
    graph: {
        (Intersection1, Intersection2): (cars waiting for Intersection1, cars waiting for Intersection2),
        ...
    }
    """
    def __init__(self, width, height, p_enter):
        self.width = width
        self.height = height
        self.p_enter = p_enter
        self.intersections = {}
        self.graph = {}
        self.corners = [
            (0,0),
            (0, self.width-1),
            (self.height-1, 0),
            (self.width-1, self.height-1)
        ]
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
        #* Determine if cars should be added to the system
        for i in self.intersections: # for each coordinate
            if i in self.corners:
                random.seed()
                if self.p_enter > random.randint(0, 100) * 0.01:
                    if random.randint(0, 100) * 0.01 < 0.5:
                        print("enter at (" + ", ".join(str(j) for j in i) + ") primary") # enter at (0, 0) primary
                        # street = self.graph[(i, self.intersections[(i[0], i[1] + 1)])]
                    else:
                        print("enter at (" + ", ".join(str(j) for j in i) + ") secondary") # enter at (0, 0) secondary
                random.seed()
                if self.p_exit > random.randint(0, 100) * 0.01:
                    if random.randint(0, 100) * 0.01 < 0.5:
                        print("exit at (" + ", ".join(str(j) for j in i) + ") primary") # exit at (0, 0) primary
                    else:
                        print("exit at (" + ", ".join(str(j) for j in i) + ") secondary") # exit at (0, 0) secondary
            elif (i[0] in [0, self.width - 1]) or (i[1] in [0, self.height - 1]): # if it is an edge coordinate
                # for each edge coordinate:
                random.seed()
                if self.p_enter > random.randint(0, 100) * 0.01:
                    print("enter at (" + ", ".join(str(j) for j in i) + ")") # enter at (0, 0)

                random.seed()
                if self.p_exit > random.randint(0, 100) * 0.01:
                    print("exit at (" + ", ".join(str(j) for j in i) + ")") # exit at (0, 0)
                    
        #* Move cars through grid
        pass

my_grid = Grid(3, 3, .1)
my_grid.step()

# for t in range(100):
#     grid.step()
