from streets.intersection import Intersection
from streets.lane import Lane
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
	def __init__(self, width, height, p_enter, street_length):
		self.width = width
		self.height = height
		self.p_enter = p_enter
		self.street_length = street_length
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

			
			try: #! Primary Axis
				intersection2 = self.intersections[(x_coord + 1, y_coord)]

				if (x_coord + 2) in range(0, self.width): ###! Lane1
					lane1 = Lane(
						intersection1,
						intersection2,
						next_intersections=(
							intersection2,
							self.intersections[(x_coord + 2, y_coord)]
						),
						length=self.street_length
					)
				else:
					lane1 = Lane(
						intersection1,
						intersection2,
						next_intersections=(
							intersection2,
							None
						),
						length=self.street_length
					)

				if (x_coord - 1) in range(0, self.width): ###! Lane2
					lane2 = Lane(
						intersection2,
						intersection1,
						next_intersections=(
							intersection1,
							self.intersections[(x_coord - 1, y_coord)]
						),
						length=self.street_length
					)
				else:
					lane2 = Lane(
						intersection2,
						intersection1,
						next_intersections=(
							intersection1,
							None
						),
						length=self.street_length
					)
				self.graph[(intersection1, intersection2)] = (lane1, lane2)
			except KeyError:
				pass

			try: #! Secondary Axis
				intersection2 = self.intersections[(x_coord, y_coord + 1)]

				if (y_coord + 2) in range(0, self.height): ###! Lane1
					lane1 = Lane(
						intersection1,
						intersection2,
						next_intersections=(
							intersection2,
							self.intersections[(x_coord, y_coord + 2)]
						),
						length=self.street_length
					)
				else:
					lane1 = Lane(
						intersection1,
						intersection2,
						next_intersections=(
							intersection2,
							None
						),
						length=self.street_length
					)

				if (y_coord - 1) in range(0, self.height): ###! Lane2
					lane2 = Lane(
						intersection2,
						intersection1,
						next_intersections=(
							intersection1,
							self.intersections[(x_coord, y_coord - 1)]
						),
						length=self.street_length
					)
				else:
					lane2 = Lane(
						intersection2,
						intersection1,
						next_intersections=(
							intersection1,
							None
						),
						length=self.street_length
					)
				self.graph[(intersection1, intersection2)] = (lane1, lane2)
			except KeyError:
				pass


	# def __str__(self):
	#     string = []
	#     for _ in range(self.width):
	#         string += "  |"
	#     string += "\n"

	#     for _ in range(self.height):
	#         for _ in range (self.width):
	#             string += "--+"
	#         string += "--"
	#         string += "\n"
	#         for _ in range(self.width):
	#             string += "  |"
	#         string += "\n"
	#     return "".join(string)
	
	def step(self):
		for i in self.intersections: #* For each pair of intersections
			if (
				i[0] in [0, self.width - 1] or
				i[1] in [0, self.height - 1]
			):
				#? HOW THE FUCK CAN THIS WORK
				print("I1: " + str(self.intersections[i]))
				print("I2: " + str(self.intersections[(i[0] + 1, i[1])]))
				# print(self.graph[(self.intersections[i], self.intersections[(i[0] + 1, i[1])])])

my_grid = Grid(3, 3, .1, 4)
my_grid.step()
print(my_grid.graph)
