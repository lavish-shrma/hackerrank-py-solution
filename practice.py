import time

name = input("Enter your Name: ").title()
hours = int(time.strftime("%H"))

if (hours>=4 and hours<12):
    print("Good morning",name)
elif(hours>=12 and hours>16):
    print("good afternoon",name)
elif(hours>=16 and hours<20):
    print("good evening",name)
else:
    print("good night",name)

# 2
    

my_day = input("enter a day to check what to-do today :- ")
x = 0

match my_day:
    case my_day if my_day == "sunday":
        print("it is %s today, so yeah you can party but not too long in night" %(my_day))
    case my_day if my_day =="monday":
        print("it is %s and its all fu*ked up to my friend" %(my_day))
    case my_day if my_day =="tuesday":
        print("it is %s and its all fu*ked up to my friend" %(my_day))
    case my_day if my_day =="wednesday":
        print("it is %s and its all fu*ked up to my friend" %(my_day))
    case my_day if my_day =="thursday":
        print("it is %s and its all fu*ked up to my friend" %(my_day))
    case my_day if my_day =="friday":
        print("it is %s and its a FRIDAY NIGHT HURREY" %(my_day))
    case my_day if my_day =="saturday":
        print("it is %s and YEAH YOU CAN PARTY TONIGHT" %(my_day))
    case _:
        print("enter a correct day name dude")