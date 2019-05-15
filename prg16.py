n=int(input("enter the limit:"))
m=int(input("enter the limit:"))
for num in range(n,m+1):
if num>1:
for i in range(2,num):
if(num%1)==0:
break;
else:
print(num)
