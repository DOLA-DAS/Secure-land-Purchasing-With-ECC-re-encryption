area=[209,262,264,279,244,234,207,245,139,295,183,129,209,200,200]
price=[735,912,1003,1065,1282,1247,1032,1235,441,964,680,439,700,439,439]


area3=area
price3=price

area1=area
price1=price
area = list(set(area))
area.sort(reverse=True)
price = list(set(price))
price.sort()
area2=[]
price2=[]
for i in range (len(area1)):
	area2.append(area.index(area1[i])+1)

for i in range (len(price1)):
	price2.append(price.index(price1[i])+1)

mx=max(area2)
nn = []
for i in range (len(area2)):
	nn.append((area2[i]+price2[i],i))

skyline_area=[]
skyline_price=[]

nn.sort()

i=0
while len(nn)!=0:
	skyline_area.append(area2[nn[i][1]])
	skyline_price.append(price2[nn[i][1]])
	
	#xmn=int(area2[nn[0][1]]),ymin=int(price2[nn[0][1]])
	k=i
	
	while k < (len(nn)):
		l=len(skyline_area)
		if(area2[nn[k][1]]>=skyline_area[l-1] and price2[nn[k][1]]>=skyline_price[l-1]):
			nn.pop(k)
			#print(nn)
			k=k
		else:
			k=k+1
		#print(nn)

skyline_area1=[]
skyline_price1=[]
for i in range (len(skyline_area)):
	skyline_area1.append(area[skyline_area[i]-1])

for i in range (len(skyline_price)):
	skyline_price1.append(price[skyline_price[i]-1])
	
print(skyline_area1)
print(skyline_price1)