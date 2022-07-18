print("Welcome to the Game")
user_1 = input("Enter Player 1 Name:\n")
user_2 = input("Enter Player 2 Name: \n")
tooth = 13
while tooth > 0:
    result =""
    for c in range(tooth):
        result +="|"
    print(result)
    print(f"There are {tooth} toothpicks left")
    t1 = int(input(f"{user_1} enter number"))
    tooth -= t1
    