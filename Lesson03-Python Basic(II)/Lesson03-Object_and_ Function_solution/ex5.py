def carbon_foot(n):
    def action(km): 
        if n=='car':
        	return 0.24*km
        elif n=='bus':
        	return 0.03*km
        else:
        	return 0.06*km
    return action

way = carbon_foot('car')
ans = way(100)
print(ans)