print("*"*30)
print("Welcome to WeekDay Game")
day=input("Enter the day of the week as: Sun,Mon,Tue,Wed,Thu,Fri,Sat ")
if day == 'sun' or day == 'Sun' or day =='Sat' or day == 'sat' :
    print(f' The {day} ,It is Weekend')
elif day == 'Mon' or day == 'mon' or  day == 'tue' or  day == 'Tue' or  day == 'wed' or  day == 'Wed' or  day == 'thu' or  day == 'Thu' or  day == 'fri' or  day == 'Fri':
    print(f"The {day} is weekday")
else :
    print(f"no day like {day}")