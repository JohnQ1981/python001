from random import randint  
print('*'*30)
print('*** WELCOME TO ROCK, PAPER AND SCISSORS GAME')
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

user=input("Enter Your Move as : rock,paper, or scissors \n")
if user == 'rock' :
    user_move = rock
elif user == 'paper':
    user_move = paper
elif user == 'scissors':
    user_move = scissors
else:
    user=input("Enter Your Move as : rock,paper, or scissors \n")

print(user_move)
print(comp_move)