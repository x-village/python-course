class Map:
	def set_map(self, n):
		self.map = [['*']*n for i in range(n)]
		self.n = n
    
	def set_pattern(self, p):
		if p==1:
			center = int(self.n / 2)
			for i in range(3):
				self.map[center-1][center-1+i]=0
			self.map[center][center-1]=0
			self.map[center+1][center]=0

	def display(self):
		for i in self.map:
			for j in i:
				print(j, end=' ')
			print()
			
my_map = Map()
my_map.set_map(5)
my_map.display()
print()
my_map.set_pattern(1) 
my_map.display()
