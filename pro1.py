def reverse(s):
str = " "
for i in s:
str = i+str
return str
s="kavi"
print("the original string is :",end=" ")
print(s)
print("thr reversed string(using loops)is:",end=" ")
print(reverse(s))
