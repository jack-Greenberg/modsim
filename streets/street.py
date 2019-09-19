class Street(object):
    """
    Represents a street in between two intersections

    i_1 (class Intersection): One intersection
    i_2 (class Intersection): Other intersection
    queue (int): Number of cars waiting on the street
    capacity (int): Number of cars allowed to wait on the street (models length of the street)
    """
    def __init__(self, i_1, i_2, queue=0, capacity=0):
        self.i_1 = i_1
        self.i_2 = i_2
        self.queue = queue
        self.capacity = capacity

    def add_car(self):
        self.queue += 1
        return self.queue
        
    def remove_car(self):
        self.queue -= 1
        return self.queue
