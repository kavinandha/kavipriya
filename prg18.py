n=int(input("enter the number:"))
m=int(input("enter the number:"))
for num in range(n,m+1)
sum=0
temp=num
while temp>0:
digit=temp%10
sum+=digit**3
temp//=10
if num ==sum:
print(num)
