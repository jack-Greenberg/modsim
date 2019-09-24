class Lane(object):
    """
    Represents a lane that cars can queue in; defined by two intersections (directional)
    
    Traffic goes from intersection_1 to intersection_2
    intersection_1 (Intersection)
    intersection_2 (Intersection)
    next_intersections (tuple, (Intersection, Intersection))
    queue = p
    """
    def __init__(self, intersection_1, intersection_2, next_intersections, length):
        self.intersection_1 = intersection_1
        self.intersection_2 = intersection_2
        self.next_intersections = next_intersections
        self.length = length
        self.queue = [ False for m in range(length) ]
