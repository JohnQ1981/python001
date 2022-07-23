print("Welcome to even or odd teller")
def evenornot(x):
    if x%2 == 0:
        return True
    return False
while True:
    enter=input("Enter number only ")
    n=evenornot(int(enter))
    if n == True:
        print(f"{n} is Even")
    else:
        print(f"{n} is Odd number")
    a=input("Do you want to play again? ")
    if a == "n" or a == "N":
        break
    else:
        continue
