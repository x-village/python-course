class Map:
	def __init__(self, n, p):
		self.map = [['*']*n for i in range(n)]
		if p==1:
			center = int(n/2)
			for i in range(3):
				self.map[center-1][center-1+i]=0
			self.map[center][center-1]=0
			self.map[center+1][center]=0
			
	def display(self):
		for i in self.map:
			for j in i:
				print(j, end=' ')
			print()
			
my_map = Map(5, 1)
my_map.display()