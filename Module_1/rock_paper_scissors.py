import random

choices = ['rock', 'paper', 'scissors']

def get_user_choice():
  user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
  while user_choice not in choices:
    user_choice = input("That's not valid. Enter rock, paper, or scissors: ").lower()
  return user_choice


def get_computer_choice():
  return random.choice(choices)


def check_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    return "It's a tie!"

    # all the combinations where the user wins
  user_wins = [
    ('rock', 'scissors'),
    ('paper', 'rock'),
    ('scissors', 'paper')
    ]

  if (user_choice, computer_choice) in user_wins:
    return " Weldone! You win!"
  else:
    return "Computer wins!"


def main():
  print("*" * 30)
  print("WELCOME TO THE ULTIMATE ROCK PAPER SCISSOR TOURNAMENT")
  print("*" * 30)
  print("ARE YOU READY TO PLAY?!!!")

  user_choice = get_user_choice()
  computer_choice = get_computer_choice()

  print("You chose:", user_choice)
  print("Computer chose:", computer_choice)

  result = check_winner(user_choice, computer_choice)
  print(result)


main()