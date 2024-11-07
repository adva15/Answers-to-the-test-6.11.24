#1
good_temp=0
avg_temp=0
highest_temp=40
low_temp=5
low_temps=[]
highest_temps=[]
while good_temp:
    try:
        for i in range(12):
            temp=int(input("temp?"))
            if not 5 <= temp <=40:
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
                print("wrong data")

    print(f"the highest temp is:{highest_temp}")
    print(f"the lowest temp is:{low_temp}")
    print(f"the average is: {avg_temp} " )

#2
counter: int = 44
country_index: int = 1
in_vote_num: int = 1
against_num: int = 2
abstained_vote=3
veto_num: int = 4
count_list: list[int] = [0]*3
options: list[str] = ["in vote", "against", "avoided"]
in_vote_index: int = None
against_index: int = None

while country_index:
    try:
        vote: int = int(input("enter your vote number:"))
        if not in_vote_num <= vote <= veto_num:
            continue
        if vote == veto_num:
            print(f"the country {country_index} voted 'veto'")
            break
        if vote == in_vote_num:
            if in_vote_index is None:
                in_favor_index = country_index
        elif vote == against_num:
            if against_index is None:
                against_index = country_index
        country_index += 1
        count_list[vote-1]+=1
    except ValueError:
        print("irrational voting")

for j in range(len(count_list)):
        print(f"total count of '{options[j]}' is:", count_list[j])



