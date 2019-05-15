def god(a,b):
if(a==b):
return n
if(a>b):
return god(a-b,b)
return god(a,b-a)
def lcm(a,b):
return (a*b)/god (a,b)  
a=int(input("a:"))
b=int(input("b:"))
print('LCM of',a,'and',a, 'is',lcm(a,b))
