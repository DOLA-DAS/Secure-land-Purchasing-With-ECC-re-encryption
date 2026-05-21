area=[209,262,264,279,244,234,207,245,139,295,183,129,209,200,200]
price=[735,912,1003,1065,1282,1247,1032,1235,441,964,680,439,700,439,439]
skyline_area=[]
skyline_price=[]
skyline_area.append(area[0])
skyline_price.append(price[0])
#print(skyline)

def is_dominated(area1,price1):
	c = 0
	for (i,j) in zip(skyline_area,skyline_price):

		if(i >= area1 and j <= price1):
			c = c + 1
	return c

def is_dominate(area1,price1):
	c = 0
	for (i,j) in zip(skyline_area,skyline_price):
		#print(area1,price1)
		if(i <= area1 and j <= price1):
			#skyline_area.remove(i)
			#skyline_price.remove(j)   
			#i=i-1
			#j=j-1
			c = c + 1
	return c

for (i,j) in zip(area,price):
	x=is_dominated(i,j)
	#print("x=",x)
	if(x==0):
		skyline_area.append(i)
		skyline_price.append(j)
		y = is_dominate(i,j)
		#print("y=",y)
		if(y>0):
			k=0
			while k < (len(skyline_area)-1):
				if(skyline_area[k]<=i and skyline_price[k]>=j):
					skyline_area.pop(k)
					skyline_price.pop(k)
					k=k   
				else:
					k+=1
					
				#print(skyline_area)
				#print(skyline_price)

print(skyline_area)
print(skyline_price)