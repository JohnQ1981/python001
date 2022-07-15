print('*'*30)
print('*** WELCOME TO ROCK, PAPER AND SCISSORS GAME')
from random import randint  
num = randint(1,3)

# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

if num == 1:
    comp_move = rock
elif num == 2:
    comp_move = paper
else :
    comp_move = scissors

print(num)

user = input("Enter Your Move as : rock,paper, or scissors \n")
if user == 'rock' :
    user_move = rock
elif user == 'paper':
    user_move = paper
elif user == 'scissors':
    user_move = scissors
else:
    user=input("Enter Your Move as : rock,paper, or scissors \n")


if (user_move == rock  and comp_move == rock) or(user_move == paper  and comp_move == paper) or (user_move == scissors  and comp_move == scissors):
    print(f"Your Move is {user_move} ")
    print(f"Computer's Move {comp_move}")
    print('it is tie')
elif user_move == rock and comp_move == scissors:
    print(f"Your Move is {user_move} ")
    print(f"Computer's Move {comp_move}")
    print('You Won')
elif user_move == rock and comp_move == paper:
    print(f"Your Move is {user_move} ")
    print(f"Computer's Move {comp_move}")
    print('You Lost')
elif user_move == paper and comp_move == rock:
    print(f"Your Move is {user_move} ")
    print(f"Computer's Move {comp_move}")
    print('You Won')
elif user_move == paper and comp_move == scissors:
    print(f"Your Move is {user_move} ")
    print(f"Computer's Move {comp_move}")
    print('You Lost')
elif user_move == scissors and comp_move == rock:
    print(f"Your Move is {user_move} ")
    print(f"Computer's Move {comp_move}")
    print('You Lost')
elif user_move == scissors and comp_move == paper:
    print(f"Your Move is {user_move} ")
    print(f"Computer's Move {comp_move}")
    print('You Won')
