print('*'*40)
age =int(input("Enter your age "))
if age >= 18 and age < 21:
    print("can enter but cannot drink ")
elif age >= 21 and age <65:
    print("can enter and buy alcohol")
elif age <18:
    print(" dude go home")
else:
    print("too old to drink")