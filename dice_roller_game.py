from random import randint
print("Welcome to DICE Roller***")
dice = int(input("How many dice your are rolling? "))
sides = int(input("How Many Sides on each dice? "))
for c in range(dice):
    #for b in range(0,sides):
    print(randint(0,sides))
again = input("Roll again? ('q' to quit)")
while again != "q":
    
    for c in range(dice):
    #for b in range(0,sides):
        randy = randint(0,sides)
        result ="|"
        result += f"{randy}|"
        print(result)
    again = input("Roll again? ('q' to quit)")
print("Bye Bye")