class Intersection(object):
    """
    position (tuple (x, y)): Position of the intersection on the grid
    light_state (bool): True if cars allowed to pass on primary axis, False if cars allowed on secondary axis
    light_timing (int): Number of seconds in a timing cycle 
    """
    def __init__(self, position):
        self.position = position
        self.queue = {'up': 0,'down': 0,'right': 0,'left': 0}

    def __str__(self):
        return str(self.queue) + '\n'

    def __repr__(self):
        return str(self.queue) + '\n'

    def update_queue(self, d, change):
        self.queue[d] += change
