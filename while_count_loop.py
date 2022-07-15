print("While count loop")
from random import randint
num = randint(0,10)
number = input("Guess Random number ")
count =1
while int(number) != num:
    number = input("Guess Random number ")
    num = randint(0,10)
    count +=1

print(f" You guessed in: {count} times and Number is :{number} and Random number is :{num}")
print("Bye Bye!")

stars =0