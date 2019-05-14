def god(x,y):
    if(y==0):
      return n
    else:
      return god(y,x% y)
x=int(input("enter x:"))
y=int(input("enter y:"))
print("the god is:",end="")
print(god(x,y))
