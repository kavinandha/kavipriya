num=[1,2,3,4,5,]
m=len(num)
num.sort()
if m%2==0:
median1=num[m//2]
median2=num[m//2-1]
median=(median1+median2)/2
else:
median=num[m//2]
print("median is:"+str(median))
