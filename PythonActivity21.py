import random

while True:
    user_action=input("Enter a choice (rock,paper,scissors):")
    possible_actions=["rock","paper","scissors"]
    computer_action=random.chpice(possible_actions)
    print(f"\nYou chpse {user_action}, computer choise {computer_action}.\n")

    if user_action==computer_action:
        print(f"Both players selected {user_action}. It's a tie!"