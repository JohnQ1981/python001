print('*'*30)
print("*** Welcome to Water Boiling Game ***")
unit = input("What unit are you using? ")
temp = input("What temperature is the water? ")
temp=int(temp)
if unit =='f' or unit =='F':
    if temp >= 212:
        print(f"Water is boiling in this {temp} of {unit}")
    else:
        print(f"Water is not boiling in this {temp} {unit} degrees")
elif unit =='k' or unit == 'K':
    if temp >= 373:
        print(f"Water is boiling in this {temp} of {unit}")
    else:
        print(f"Water is not boiling in this {temp} {unit} degrees")
elif unit=='c' or unit =="C" :
    if temp>= 100:
        print(f"Water Does boil in {temp} {unit} degrees")
    else:
        print(f"Water is not boiling in this {temp} {unit} degrees")
else:
    print(f'Wrong Type of {unit} Unit Entered')