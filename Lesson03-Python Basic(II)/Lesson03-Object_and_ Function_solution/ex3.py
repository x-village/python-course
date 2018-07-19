def f(a, b):
	if a<b:	
		return 'a<b'
	elif a==b:
		return 'a=b'
	else:
		return 'a>b'

a = 1
b = 2	
result = f(a, b)
print(result)