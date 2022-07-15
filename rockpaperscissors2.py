from random import randint
print("*"*30)
print("*** WELCOME TO ROCK PAPER SCISSORS GAME ***")
num = randint(1,3)
#trun that random number into the computer's RPS Move
if num == 1:
    comp_move='rock'
elif num ==2:
    comp_move ='paper'
elif num ==3:
    comp_move = 'scissors'

# moves assignments
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
            """

paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
            """
        

scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
            """
#ask user to enter their move
user_move = input("Enter your move as: rock, paper, or scissors ").lower()
#print the rock , paper, or scissors ASCII art that corresponds to the user's move
if user_move=='rock':
    print(rock)
elif
