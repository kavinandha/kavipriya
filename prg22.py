def largest(arr,n):
  max=arr[0]
  for i in range(1,n):
    if arr[i]>max:
      max=arr[i]
  return max
n=int(input("enter the N number:"))
arr=list(map(int,input("enter the number:").split()))
ans=largest(arr,n)
print("largest in given array is",ans)
