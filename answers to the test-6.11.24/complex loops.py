temp=0
good_temp=0
avg_temp=0
highest_temp=40
low_temp=5
low_temps=[]
highest_temps=[]
try:
    for i in range(12):
        temp=int(input("temp?"))
        if not 5<= temp <=40:
            print("wrong data")
        else:
            print("correct data")
        if 5 <= temp <= 40:
            continue
        good_temp+=1
        if 0 in range(2):
         break
        if temp>highest_temp:
            highest_temp=temp
            highest_temps.append(temp)
        elif  temp<low_temp:
            low_temp=temp
            low_temps.append(temp)
            avg_temp=highest_temp/low_temp
except ValueError:
            print("data")

print(f"the highest temp is:{highest_temp}")
print(f"the lowest temp is:{low_temp}")
print(f"the average is: {avg_temp} " )