print("*"*40)
print("*** WELCOME TO ROCK PAPER SCISSORS GAME *** \n")
from random import randint 
random_number = randint(1,3)
print(random_number)
user= input("Enter your Move as: 'rock', 'paper', or 'scissors'\n ")
if random_number==1:
    computer ='rock'
elif random_number==2:
    computer = 'paper'
else:
    computer = 'scissors'

print(f"Computer chose: {computer}")

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

your_move="Your move"
computer_move="Computer's move"

if user =='rock' and random_number == 1:
    # Rock
    print(your_move)
    print(rock)
    print(computer_move)
    print(rock)
    print('it is tie')
elif user =='paper' and random_number == 1:
    # Paper
    print(your_move)
    print(paper)
    print(computer_move)
    print(rock)
    print("You won, computer lost")
elif user =='scissors' and random_number == 1 :
    # Scissors
    print("Your Move")
    print(scissors)
    print("computer's Move")
    print(rock)
    print("You lost, computer won")

if user =='rock' and random_number == 2:
    # Rock
    print("Your Move")
    print(rock)
    print("Computer's Move")
    print(paper)
    print('You lost, computer won')
elif user =='paper' and random_number == 2:
    # Paper
    print("Your Move")
    print(paper)
    print("Computer's Move")
    print(paper)
    print("it is tie")
elif user =='scissors' and random_number == 2 :
    # Scissors
    print("Your Move")
    print(scissors)
    print("Computer's Move")
    print(paper)
    print("You won, computer lost")




if user =='rock' and random_number == 3:
    # Rock
    print(rock)
    print("Computer's Move")
    print(scissors)
    print('You won, computer lost')
elif user =='paper' and random_number == 3:
    # Paper
    print(paper)
    print("Computer's Move")
    print(scissors)
    print("You lost, computer won")
elif user =='scissors' and random_number == 3 :
    # Scissors
    print(scissors)
    print("Computer's Move")
    print(scissors)
    print("it is tie")