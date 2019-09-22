class Intersection(object):
    """
    position (tuple (x, y)): Position of the intersection on the grid
    light_state (bool): True if cars allowed to pass on primary axis, False if cars allowed on secondary axis
    light_timing (int): Number of seconds in a timing cycle 
    cars (tuple (n, e, s, w)): Number of cars at each of the parts of the intersection
    """
    def __init__(self, position, light_timing, light_state=True):
        self.position = position
        self.light_state = light_state
        self.light_timing = light_timing

    def __str__(self):
        return ",".join(str(m) for m in self.position)

    def __repr__(self):
        return ",".join(str(m) for m in self.position)

    def change_light(self):
        self.light_state = not self.light_state
