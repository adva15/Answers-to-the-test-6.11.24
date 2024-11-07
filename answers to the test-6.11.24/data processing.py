#1
amount=0
sentinel=-99
while True:
    number:int=int(input("number?"))
    if number==sentinel:
        print("None")
        break
    if number >0:
        amount+=number
        print("the amount of sum numbers:",amount)

#2
numbers=[]
count:list[float] = []
SENTINEL: int = -99
while True:
    number: float = float(input('enter number:'))
    if number==SENTINEL:
        break
    if number<0:
          continue
    print(f"The highest value is == {max(numbers)}")
    print(f"The lowest value is == {min(numbers)}")

#3
number_3=[]
numbers_3=[]
for _ in range(5):
    numbers_3 = int(input("enter numbers:"))
    number_3.append(numbers_3)

maximum_3=max(number_3)
index_max=number_3.index(maximum_3)+1

print(index_max)

#4
num_x:int=int(input("number 1:"))
num_y:int=int(input("number 2:"))

sum_x_y:int=num_x+num_y
print(sum_x_y)

#5
num_a:int=int(input("number 1:"))
num_b:int=int(input("number 2:"))
sum_result=1
for h in range(num_b):
    sum_result*=num_a
print(sum_result)

#6
numbers:int = int(input("enter numbers:"))
digit:int = int(input("enter digit:"))
while numbers:
    if numbers % 10 == digit:
        print(True)
        break
    numbers //= 10
else:
    print(False)

#7
num_1: int = int(input("Enter  number 1:"))
num_2: int = int(input("Enter  number 2:"))
if num_1 > num_2:
    for i in range(num_2 , 0, -1):
        if num_1 % i == 0 and num_2 % i == 0:
            print(f"highest divider: {i}")
            break
else:
    for _ in range(num_1 , 0, -1):
        if num_2 % _ == 0 and num_1 % _ == 0:
            print(f"highest divider: {_}")
            break


#8
is_prime: bool = True
x: int = int(input("enter  number:"))
if x == 2:
    print("prime")
    is_prime = True
elif x % 2 == 0:
    is_prime = False

print(f"{x} is {"prime" if is_prime else "not prime"}")






