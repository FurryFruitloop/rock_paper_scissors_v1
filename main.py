rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice == 0:
  print(rock)
if user_choice == 1:
  print(paper)
if user_choice == 2:
  print(scissors)

computer_choice = random.randint(0, 2)

print("Computer chose:")
if computer_choice == 0:
  print(rock)
  if user_choice == 0:
    print("Draw")
  elif user_choice == 1:
    print("You won!")
  elif user_choice == 2:
    print("You lose!")
if computer_choice == 1:
  print(paper)
  if user_choice == 0:
    print("You lose!")
  elif user_choice == 1:
    print("Draw")
  elif user_choice == 2:
    print("You won!")
if computer_choice == 2:
  print(scissors)
  if user_choice == 0:
    print("You won!")
  elif user_choice == 1:
    print("You lose!")
  elif user_choice == 2:
    print("Draw")

#conditions for winning and losing:
  #winning: 0 against 2, 1 against 0, 2 against 1
  #losing: 0 against 1, 1 against 2, 2 against 0
  #draw: against self