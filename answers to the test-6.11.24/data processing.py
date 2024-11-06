# #1
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
    numbers.append(number)
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





