area=[209,262,264,279,244,234,207,245,139,295,183,129]
price=[735,912,1003,1065,1282,1247,1032,1235,441,964,680,439]

area1=area
price1=price
area = list((area))
area.sort(reverse=True)
price = list((price))
price.sort()
area2=[]
price2=[]



for i in range (len(area1)):
	area2.append(area.index(area1[i])+1)

for i in range (len(price1)):
	price2.append(price.index(price1[i])+1)

list1=[]
list2=[]
for i in range (len(area2)):
	if(area2[i]<price2[i]):
		list1.append((area2[i],price2[i]))
	else: 
		list2.append((area2[i],price2[i]))

list1.sort()
list2.sort(key = lambda x: x[1])

print(list1)
print(list2)

skyline_point=[]





skyline_point.append(list1[0])

skyline_point.append(list2[0])



def dominated(a,p):
	c = 0
	i=0
	while i < (len(skyline_point)):

		if(skyline_point[i][0] <= a and skyline_point[i][1] <= p):
			c = c + 1
		i=i+1
	return c
i=1
l1=0
l2=0
while i < max(len(list1),len(list2)):
	if l1==1 and l2==1:
		break
	if l1==0:
		if((list1[i][0]>=list1[i-1][0]) and (list1[i][0]>=list1[i-1][1])):
			l1=l1+1
		else:
			x=dominated(list1[i][0],list1[i][1])
			if x==0:
				skyline_point.append(list1[i])
		if i==(len(list1)):
			l1=l1+1
	if l2==0:
		if((list2[i][0]>=list2[i-1][0]) and (list2[i][0]>=list2[i-1][1])):
			l2=l2+1
		else:
			x=dominated(list2[i][0],list2[i][1])
			if(x==0):
				skyline_point.append(list2[i])
		if i==(len(list2)):
			l2=l2+1
	i=i+1		

		
skyline_area1=[]
skyline_price1=[]
for i in range (len(skyline_point)):
	skyline_area1.append(area[skyline_point[i][0]-1])

for i in range (len(skyline_point)):
	skyline_price1.append(price[skyline_point[i][1]-1])
print(skyline_area1)
print(skyline_price1)