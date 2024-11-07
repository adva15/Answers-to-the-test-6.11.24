#1
num1:float=float(input("number 1:"))
num2:float=float(input("number 2:"))

if num1<num2:
     print(num1)
     print(num1)
     print(num1)
else:
    print(num2)
    print(num2)
    print(num2)

#2
num_1:int=int(input("number 1:"))
num_2:int=int(input("number 2:"))

avg_numbers=(num_1+num_2)//2
print("the average is:",avg_numbers)

#3
num1:float=float(input("number 1:"))
num2:float=float(input("number 2:"))
num3:float=float(input("number 3:"))

print(max(num1,num2,num3))

#4
movie:int=(int(input("what's time the movie?")))

time:int=movie//60
minutes:int=movie%60

print(f"time {time} minutes {minutes}")

#5
number_4_d: int = int(input("enter 4 digits number:"))
Right_d= number_4_d % 10
print("Right digit is",Right_d)

#6
number_4_d: int = int(input("enter 4 digits number:"))
Right_2_d= number_4_d % 100//10
print("Right 2 digit is",Right_2_d)

#7
double_digits:int=int(input("enter double digit numbers:"))
ahadot=double_digits % 10
asarot=double_digits // 10

sum_double_digits=ahadot+asarot
print("sum=",sum_double_digits)

#8
swap_digits:int=int(input("enter 2 digits numbers:"))
ahadot=swap_digits%10
asarot=swap_digits//10

new_number: int = ahadot * 10 + asarot
print(f"swap={new_number}")

#9
zugi_or_e_zugi:int=int(input("enter  zugi or e zugi numbers:"))
if zugi_or_e_zugi %2==0:
    print("even")
else:
    print("odd")

#10
salary = int(input("enter salary to pay:"))
tax= 0
income = salary

if income < 6_000:
    tax = 0
else:
    salary -= 6_000
if income > 12_000:
    tax += 6_000 * 0.1
    salary -= 6_000
if income > 18_000:
    tax += 6_000 * 0.2
    salary -= 6_000
if income > 25_000:
    tax += 7_000 * 0.3
    salary -= 7_000
if income > 35_000:
        tax += 10_000 * 0.4
        salary -= 10_000
if income > 50_000:
        tax += 15_000 * 0.45
        salary -= 15_000
if income > 50_000:
        tax += salary * 0.51

print(f" Total tax {income} are : {tax}")

#11
can_up=0
age:int=int(input("enter age:"))
height:float=float(input("enter height:"))
if 8 <= age <= 18 and height >= 115:
    can_up +=1
else:
    if age > 18 and height > 100:
     can_up +=1
print(f"you {"can" if can_up else "can't"} go up on the roller coaster")

