#1
# top:int=int(input("natural number:"))
#
# for i in range(1,top+1):
#     print(i,end="")
# print()

#2
num_x:int=int(input(" number 1:"))
num_y:int=int(input(" number 2:"))

first=min(num_x,num_y,2)
last=max(num_x,num_y,2)
for _ in range(first,last,2):
    print(_,end="")
print()

#3
num_x:int=int(input(" number 1:"))
num_y:int=int(input(" number 2:"))

for j in range(num_x,num_y+1):
    if j %2 ==0:
     print(j,end="")
print()

