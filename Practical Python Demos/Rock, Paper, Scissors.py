import random

computer_choice = random.choice (['rock', 'paper', 'scissors'])
user_choice = input("Choose rock, paper, or scissors")


if user_choice == computer_choice:
    print("Tie")

elif user_choice == "rock" and computer_choice == "scissors":
    print("You Win")

elif user_choice == "paper" and computer_choice == "rock":
    print("You Win")

elif user_choice == "scissors" and computer_choice == "paper":
    print("You Win")

else:
    print("You Lose")           
