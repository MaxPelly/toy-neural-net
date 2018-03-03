from random import uniform

class Matrix(object):
	def __init__(self, rows, collumns, random = False):
		self.rows = rows
		self. cols = collumns
		self.data = [[0 for __ in range(collumns)] for _ in range(rows)]
		if random:
			self.randomise()
		
	def __repr__(self):
		return str(self.data)
		
	def __add__(self, other):
		output = matrix(self.rows, self.cols)
		if isinstance(other, Matrix):
			assert self.rows == other.rows and self.cols == other.cols
			for collumn in range(self.cols):
				for row in range(self.rows):
					output[collumn][row] = self.data[collumn][row] + other.data[collumn][row]
					
		elif isinstance(other, int) or isinstance(other, float):
			for collumn in range(self.cols):
				for row in range(self.rows):
					output[collumn][row] = self.data[collumn][row] + other
					
		return output
	
	def __radd__(self, other):
		return self.__add__(other)
		
	def add(self, other):
		self = self + other
		
	def __mul__(self, other):
		if isinstance(other, Matrix):
			pass
			
		if isinstance(other, int) or isinstance(other, float):
			output = matrix(self.rows, self.cols)
			for collumn in range(self.cols):
				for row in range(self.rows):
					output[collumn][row] = self.data[collumn][row] * other
					
			return output
				
	def __rmul__(self, other):
		return self.__mul__(other)
		
	def mul(self, other):
		self = self * other
		
	def randomise(self):
		for collumn in range(self.cols):
				for row in range(self.rows):
					self.data[collumn][row] = uniform(-1, 1)
