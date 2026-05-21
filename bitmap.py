area=[209,262,264,279,244,234,207,245,139,295,183,129,209,200,200]
price=[735,912,1003,1065,1282,1247,1032,1235,441,964,680,439,700,439,439]



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

for i in range (len(area1)):
	if(area2[i]==area2[i-1] and price2[i]==price2[i-1]):
		area2[i]=area2[i]+1
		price2[i]=price2[i]+1


area3=[]
price3=[]
x=len(area)+1
str1=""
for i in range (len(area2)):
	x1=x-(area2[i]+1)+1
	for j in range (x1):
		str1+="1"
	for k in range ((x-x1)-1):
		str1+="0"
	area3.append(str1)
	str1=""

str2=""
for i in range (len(price2)):
	x2=x-(price2[i]+1)+1
	for j in range (x2):
		str2+="1"
	for k in range ((x-x2)-1):
		str2+="0"
	price3.append(str2)
	str2=""	
#for i in range (len(area3)):
	#print(area3[i],price3[i])
	#i+=1


def f1(xx,yy):
	str3=""
	str4=""
	str7=""
	for i in range (len(area3)):
		str5=area3[i]
		x5=x-xx
		x5=x5-1
		str3+=str5[x5]
	for i in range (len(price3)):
		str6=price3[i]
		x6=x-yy
		x6=x6-1
		str4+=str6[x6]
	for i in range (len(str3)):
		if(str3[i]=='1' and str4[i]=='1'):
			str7+='1'
		else:
			str7+='0'

	c=0
	for i in range (len(str7)):
		if(str7[i]=='1'):
			c+=1
	return c

skyline_area=[]
skyline_price=[]

for i in range (len(area2)):
	ans= f1(area2[i],price2[i])
	if(ans==1):
		skyline_area.append(area1[i])
		skyline_price.append(price1[i])


print(skyline_area)
print(skyline_price)