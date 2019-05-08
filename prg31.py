input_string=input("enter a string:")
count=0
for c in input_string:
    if c.isspace()!=true:
      count=count+1
print("total number of character:",count)
