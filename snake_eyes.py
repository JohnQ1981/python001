print("*"*40)
print("Welcome to Dice Game-Snake Eyes")
from random import randint
snake_1 = randint(1,6)
snake_2 = randint(1,6)
count =1
while snake_1 != 1 or snake_2 != 1 :
    print(snake_1 , snake_2)
    print("*"* snake_1)
    print("-"* snake_2)
    snake_1 = randint(1,6)
    snake_2 = randint(1,6)
    count +=1

print(snake_1 , snake_2)
print(f"Did roll at {count} times")
