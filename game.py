import random

user_score = 0
computer_score = 0

print("=== ROCK PAPER SCISSORS GAME ===")
print("Instructions:")
print("Choose Rock, Paper, or Scissors.")
print("Rock beats Scissors")
print("Scissors beats Paper")
print("Paper beats Rock")

while True:
    user_choice = input("\nEnter Rock, Paper, or Scissors: ").lower()

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please try again.")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])

    print("You chose:", user_choice.capitalize())
    print("Computer chose:", computer_choice.capitalize())

    if user_choice == computer_choice:
        print("It's a Tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You Win!")
        user_score += 1
    else:
        print("Computer Wins!")
        computer_score += 1

    print("\nScore:")
    print("You:", user_score)
    print("Computer:", computer_score)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nFinal Score:")
        print("You:", user_score)
        print("Computer:", computer_score)
        print("Thanks for playing!")
        break