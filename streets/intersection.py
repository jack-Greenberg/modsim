class Intersection(object):
    """
    position (tuple (x, y)): Position of the intersection on the grid
    light_state (bool): True if cars allowed horizontally, False if cars allowed vertially
    light_timing (int): Number of seconds in a timing cycle 
    cars (tuple (n, e, s, w)): Number of cars at each of the parts of the intersection
    """
    def __init__(self, position, light_timing, light_state=True):
        self.position = position
        self.light_state = light_state
        self.light_timing = light_timing

    def change_light(self):
        self.light_state = not self.light_state
