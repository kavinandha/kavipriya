class solution(object):
def reverse(self,x):
type x:int
rtype: int
negative=false
if(x<0):
x=x*-1
negative=true
else:
x=x
sum=0
dig =1
strx=str(x)
1st=list(strx)
for i in lst:
sum+=int(i)*dig
if(abs(sum)>2**32):
return sum*-1
else:
return sum
