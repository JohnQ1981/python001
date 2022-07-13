print('*'*30)
print('*** Practice Nested if s ***')
month=input('Enter Month of the Year ')
if month == 'January' or month =='january':
    print('It is winter ')
    days=input(f"Enter How many Days do you think does {month} has? ")
    days=int(days)
    if days==31:
        print(f'Correct , your {days} is the same with January days')
    elif days<31:
        print(f'Your {days} is {31-days} days less than {month}')
    else:
        print(f'Your {days} is {days-31} days longer than {month}')
elif month =='February' or month=="february":
    print('still winter but feb')
