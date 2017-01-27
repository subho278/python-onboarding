'''

A Vector class will be used to represent a vector in n-dimensional space. You should be allowed to initialize
a vector by passing a list or a tuple or any iterable of numbers. All the following tests must pass.


>>> v = Vector([10, 2])
>>> v
Vector((10, 2))

>>> v = Vector([10, 2, 13, 18])
>>> v.dimension
4

>>> v = Vector([10, 2])
>>> w = Vector((10, 2))
>>> v == w
True

>>> v = Vector([10, 2])
>>> w = Vector([10, 3])
>>> v == w
False

>>> v = Vector([8, 2])
>>> w = Vector([10, 3])
>>> v + w
Vector((18, 5))

>>> v = Vector([8, 2])
>>> w = Vector([10, 3])
>>> v - w
Vector((-2, -1))

The magnitude of a vector is the square root of the sum of the squares.
>>> v = Vector([3, 4])
>>> v.magnitude()
5.0

The direction of a vector is the unit vector parallel to the same vector in the same direction.
The magnitude of the unit vector should be 1.
>>> v = Vector([3, 4])
>>> v.direction().magnitude()
1.0

Implement scalar multiplication for vectors. Multiplication should be supported both ways. 2 * v = v * 2
>>> v = Vector([3, 4])
>>> v * 2
Vector((6, 8))

>>> v = Vector([3, 4])
>>> 2 * v
Vector((6, 8))

>>> v = Vector([3, 4])
>>> 2 * v
Vector((6, 8))

>>> v = Vector([3, 4])
>>> v * 5 == 5 * v
True

Implement dot product for vectors. This should do a summation element wise. (2, 3) * (4, 5) = 2 * 4 + 3 * 5
>>> v = Vector([3, 4])
>>> w = Vector([7, 8])
>>> v * w
53

>>> v = Vector([3, 4])
>>> w = Vector([7, 8])
>>> w * v
53

You should not be allowed to do a dot product of vectors with non matching dimensions
>>> v = Vector([3, 4])
>>> w = Vector([7, 8, 9])
>>> v * w
Traceback (most recent call last):
...
ValueError: Non matching vector dimensions

Check if vector is parallel to another vector. Implement the is_parallel_to method.
The angle between two vectors can determined from the formula v .* w = |v||w|cos(theta) where left side is the dot
product and |v| represents the magnitude of v
>>> v = Vector((-2.328, -7.284, -1.214))
>>> w = Vector((-1.821, 1.072, -2.94))
>>> v.is_parallel_to(w)
False

>>> v = Vector((-7.579, -7.88))
>>> w = Vector((22.737, 23.64))
>>> v.is_parallel_to(w)
True

Implement the is_orthogonal_to method to check if a vector is perpendicular to another vector
>>> v = Vector((-2.328, -7.284, -1.214))
>>> w = Vector((-1.821, 1.072, -2.94))
>>> v.is_orthogonal_to(w)
True



'''

# Write your code here
import math
import itertools

class Vector:
	"""docstring for Vector"""
	def __init__(self, args): #class is initialized
		self.args = args
		self.dimension = len(self.args)

	def __str__(self): #string representation of the object
		return 'Vector('+ str(tuple(self.args)) + ')'

	def __repr__(self):
		return str(self)

	def magnitude(self):
		mag_sq = reduce(lambda x,y: x**2 + y**2, self.args)
		mag = math.sqrt(mag_sq)
		return mag

	def direction(self):
		magnitude = self.magnitude()
		direc = [x/float(magnitude) for x in self.args]
		direc_vector = Vector(direc)
		return direc_vector

	def __eq__(self, other): #equal operator is overriden
		if self.dimension != other.dimension:
			return False

		else:
			len = self.dimension
			for i in range(len):
				if self.args[i] != other.args[i]:
					return False

			return True

	def __add__(self, other): #add operator is overriden
		s = [x+y for x,y in itertools.izip_longest(list(self.args), list(other.args), fillvalue=0)]
		s_vector = Vector(s)
		return s_vector

	def __sub__(self, other): #subtract operator is overriden
		d = [x-y for x,y in itertools.izip_longest(list(self.args), list(other.args), fillvalue=0)]
		d_vector = Vector(d)
		return d_vector

	def __mul__(self, other): #multiply operator is overriden
		if isinstance(other, int):
			m = [x*other for x in self.args]
			m_vector = Vector(m)
			return m_vector

		elif self.dimension != other.dimension:
			raise ValueError('Non matching vector dimensions')

		else:
			len = self.dimension
			m = 0
			for i in range(len):
				val = int(self.args[i] * other.args[i] * 1000)/float(1000)
				m += val

			if m.is_integer():
				return int(m)
			else:
				return m

	def __rmul__(self, other): #reverse multiplication is overriden, for maintaining commutative property of scalar and dot product
		if isinstance(other, int):
			m = [x*other for x in self.args]
			m_vector = Vector(m)
			return m_vector

		elif self.dimension != other.dimension:
			raise ValueError('Non matching vector dimensions')

		else:
			len = self.dimension
			m = 0
			for i in range(len):
				val = int(self.args[i] * other.args[i] * 1000)/float(1000)
				m += val

			if m.is_integer():
				return int(m)
			else:
				return m

	def is_parallel_to(self, other): #checks if two vectors are parallel or antiparallel, comparison upto 3 decimal places
		self_mag = self.magnitude()
		other_mag = other.magnitude()
		dot_product_mag = math.fabs(self * other)
		m = int(self_mag * other_mag * 1000)/float(1000)
		if (dot_product_mag == m):
			return True
		else:
			return False

	def is_orthogonal_to(self, other): #checks if two vectors are orthogonal, comparison upto 3 decimal places
		dot_product = self * other
		if (dot_product == 0):
			return True
		else:
			return False		

# Do not change code after this line

if __name__ == '__main__':
    import doctest
    doctest.testmod()
