def f(n):
    if n==1:
        return 1
    elif n==0:
    	return 0
    else:
        return f(n-1)+f(n-2)

print('answer: ',f(20))