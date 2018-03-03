from perceptron import Perceptron
from random import randint
 
size = (500, 300)

p = Perceptron(2)

class Point (object):
	def __init__(self, x, y):
		self.position = (x, y)
		if y > self.f(x):
			self.label = 1
		else:
			self.label = -1
			
	def f(self, x):
		return 3 * x + 2

points = [Point(randint(0, size[0]),randint(0, size[0])) for p in range(20)]

sum = 0						
for point in points:
	if p(point.position) == point.label:
		sum += 1
print(sum/len(points))
	
print('training')

points = [Point(randint(0, size[0]),randint(0, size[0])) for p in range(1000)]

for point in points:
	p.train(point.position, point.label)
	
points = [Point(randint(0, size[0]),randint(0, size[0])) for p in range(20)]

sum = 0
for point in points:
	if p(point.position) == point.label:
		sum += 1
print(sum/len(points))



