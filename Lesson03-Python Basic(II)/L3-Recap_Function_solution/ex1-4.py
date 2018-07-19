def f(score, work_overtime):
	if score>90:
		subtotal = 8000
	elif score>=70 and score<=90:
		subtotal = 6000
	else:
		subtotal = 4000
		
	return subtotal + work_overtime*200
	
print('A:', f(45, 14))
print('B:', f(95, 13))
print('C:', f(88, 22))