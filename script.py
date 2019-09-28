from streets.intersection import Intersection
from streets.lane import Lane
import random

def flip(p):
	random.seed()
	if (random.randint(0, 100) * 0.01) < p:
		return True
	else:
		return False

class CapacityError(Exception):
	pass

class Grid(object):
	"""
	width (int): Number of intersections on the x-axis
	height (int): Number of intersections on the y-axis
	p_enter (float): Probability that a car enters the grid
	p_exit (float): Probability that a car exits the grid
	street_length (int): Number of cars each street can hold
	light_state (bool)

	intersections: {
		(x_coord, y_coord): Intersection((x, y), queue=(0,0,0,0)),
		...
	}
	"""
	def __init__(self, width, height, p_enter, street_length, light_timing, light_state=False):
		self.width = width
		self.height = height
		self.p_enter = p_enter
		self.street_length = street_length
		self.intersections = {}
		self.light_timing = light_timing
		self.light_state = light_state

		self.corners = [
			(0, 0),
			(self.width - 1, 0),
			(0, self.height - 1),
			(self.width - 1, self.height - 1)
		]

		square = [ (i, j) for i in range(width) for j in range(height) if i in [0, width - 1] or j in [0, height - 1]  ]
		self.edges = list(set(square) - set(self.corners))

		for i in range(width):
			for j in range(height):
				self.intersections[(i, j)] = Intersection((i, j))

	def step(self, time):
		if (time != 0) and (time % self.light_timing == 0):
			self.light_state = not self.light_state

		for coordinate_pair in self.intersections:
			if coordinate_pair in self.edges: # An edge
				if flip(self.p_enter):
					if coordinate_pair[0] == 0:
						self.intersections[coordinate_pair].update_queue('right', 1)
					elif coordinate_pair[0] == self.width - 1:
						self.intersections[coordinate_pair].update_queue('left', 1)
					elif coordinate_pair[1] == 0:
						self.intersections[coordinate_pair].update_queue('up', 1)
					elif coordinate_pair[1] == self.height - 1:
						self.intersections[coordinate_pair].update_queue('down', 1)
			elif coordinate_pair in self.corners: # A corner
				if flip(self.p_enter):
					if flip(.5):
						# Primary
						if (coordinate_pair == (0, 0)):
							self.intersections[coordinate_pair].update_queue('up', 1)
						elif (coordinate_pair == (self.width - 1, 0)):
							self.intersections[coordinate_pair].update_queue('up', 1)
						elif (coordinate_pair == (0, self.height - 1)):
							self.intersections[coordinate_pair].update_queue('down', 1)
						elif (coordinate_pair == (self.width - 1, self.height - 1)):
							self.intersections[coordinate_pair].update_queue('down', 1)
					else:
						# Secondary
						if (coordinate_pair == (0, 0)):
							self.intersections[coordinate_pair].update_queue('right', 1)
						elif (coordinate_pair == (self.width - 1, 0)):
							self.intersections[coordinate_pair].update_queue('left', 1)
						elif (coordinate_pair == (0, self.height - 1)):
							self.intersections[coordinate_pair].update_queue('right', 1)
						elif (coordinate_pair == (self.width - 1, self.height - 1)):
							self.intersections[coordinate_pair].update_queue('left', 1)

			if self.light_state == True:
				#* True means cars can go up or down 
				#* False means cars can go left or right
				for d in ['up', 'down']:
					if self.intersections[coordinate_pair].queue[d] > 0:
						x = self.intersections[coordinate_pair].position[0]
						y = self.intersections[coordinate_pair].position[1]
						y_direction = 1 if d is 'up' else - 1
						try:
							#! The next intersection exists!
							has_space = bool(self.intersections[(x, y + y_direction)].queue[d] <= self.street_length)
							if has_space:
								self.intersections[coordinate_pair].update_queue(d, -1)
								self.intersections[(x, y + y_direction)].update_queue(d, 1)
							else:
								raise CapacityError("Not enough space at the desired intersection; car cannot pass.")
						except KeyError:
							#! The next intersection doesn't exist :(
							self.intersections[coordinate_pair].update_queue(d, -1)
						except CapacityError:
							print("Capacity Error happened, continuing...")
			else:
				for d in ['left', 'right']:
					if self.intersections[coordinate_pair].queue[d] > 0:
						x = self.intersections[coordinate_pair].position[0]
						y = self.intersections[coordinate_pair].position[1]
						x_direction = 1 if d is 'right' else - 1
						try:
							#! The next intersection exists!
							has_space = bool(self.intersections[(x + x_direction, y)].queue[d] <= self.street_length)
							if has_space:
								self.intersections[coordinate_pair].update_queue(d, -1)
								self.intersections[(x + x_direction, y)].update_queue(d, 1)
							else:
								raise CapacityError("Not enough space at the desired intersection; car cannot pass.")
						except KeyError:
							#! The next intersection doesn't exist :(
							self.intersections[coordinate_pair].update_queue(d, -1)
						except CapacityError:
							print("Capacity Error happened, continuing...")

my_grid = Grid(3, 3, .8, 5, 5)

for t in range(100):
	random.seed()
	my_grid.step(t)

print(my_grid.intersections)
