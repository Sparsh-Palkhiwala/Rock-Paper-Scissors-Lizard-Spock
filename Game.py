import random

user_choice = input("What do you choose ? Rock Paper Scissors Lizard or Spock ")

computer_choice = random.choice(["Rock","Paper","Scissors","Lizard","Spock"])

print("User goes with :",user_choice)

print("Computer goes with :",computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win!")
elif user_choice == "lizard" and computer_choice == "scissors":
    print("You win!")
elif user_choice == "spock" and computer_choice == "lizard":
    print("You win!")
else:
    print("Computer wins!")