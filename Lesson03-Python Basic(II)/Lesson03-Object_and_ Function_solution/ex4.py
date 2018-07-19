def maker(n):
     return lambda x: n ** x
    
f = maker(9)
a = f(5)
print(a)