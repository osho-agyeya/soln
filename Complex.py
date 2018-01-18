import math

class complex_number():

	def __init__(self,x,y=0.0):
		self.x=x
		self.y=y

	def __str__(self):
		if(self.y>=0):
			return '%s+%si' % (self.x,self.y)
		else:
			return '%s%si' % (self.x,self.y)

	def __add__(self,self1):
		return complex_number(self.x+self1.x,self.y+self1.y)

	def __sub__(self,self1):
		return complex_number(self.x-self1.x,self.y-self1.y)

	def __mul__(self,self1):
		return complex_number(self.x * self1.x - self.y * self1.y, self.x * self1.y + self.y * self1.x)

	def __truediv__(self,self1):
		deno=self1.x**2 + self1.y**2
		try:
			return complex_number((self.x * self1.x + self.y * self1.y)/deno, -1*(self.x * self1.y - self.y * self1.x)/deno)
		except:
			print("Division by zero error")

	def __abs__(self):
		return math.sqrt(self.x**2 + self.y**2)

	def real(self):
		return self.x

	def imag(self):
		return self.y

	def argument(self): #in radians
		try:
			return math.atan(self.y/self.x)
		except:
			if self.x==0 and self.y>0:
				return ((22/7)/2)
			elif self.x==0 and self.y<0:
				return (-1*(22/7)/2)
			else:
				print("Division by zero error")

	def conjugate(self):
		return complex_number(self.x,-1*self.y)