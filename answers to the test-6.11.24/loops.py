#1
top:int=int(input("natural number:"))

for i in range(1,top+1):
    print(i,end="")
print()

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

#4
max_x:int=int(input("max number 1:"))
den:int=int(input("den number 2:"))

print(f"The numbers that are divisible by den up to the maximum:", end="")
for k in range(0, max_x + 1):
    if k % den == 0:
         print(k,'', end="")
print()



