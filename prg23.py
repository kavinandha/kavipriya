def min(list1,m):
final_list=[];
for i in range(0,m):
min1=9999999;
for j in range(len(list1)):
if list1[j]<min1:
min1=list[j]
list1.remove(min1);
print(final_list)
list1=(4,78,34,10,8,21,11,231);
m=2;
min(list1,m)
