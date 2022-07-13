import random
from random import randint
print("*"*25)
print("Welcome to Random Number Guess Game!!!")
random_n=random.randint(0,100)
print(random_n)
guess=input("Enter Guessed Number\n")
guess=int(guess)
count=0

if random_n == guess:
    count +=1
    print(f'You got it in {count} guess ')
    
else:
    print('Try again')
    count +=1
