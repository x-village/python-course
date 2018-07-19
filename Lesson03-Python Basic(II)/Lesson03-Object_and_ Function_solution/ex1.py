def f(n):
	for i in range(1, n+1):
		for j in range(1, n+1):
			print(i, '*', j, '=', i*j, end='\t')
		print()
f(10)