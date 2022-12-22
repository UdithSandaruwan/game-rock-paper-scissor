import random

def choice():
  player_choice = input("Enter a choice (rock, paper, scissor): ")
  options = ["rock", "paper", "scissor"]
  computer_choice = random.choice(options)
  choice = {"player": player_choice, "computer": computer_choice}
  return choice

def selection(user,computer):
    print(f"your choice {user} ; computer choice {computer}")
    if user == computer:
        return "you are lose the game ... !"
    elif user == "rock":
        if computer == "paper":
            return "you are lose the game ... !"
        else:
            return "you are win the game ... !"
    elif user == "paper":
        if computer == "rock":
            return "you are win the game ... !"
        else:
            return "you are lose the game ... !"
    elif user == "scissor":
        if computer == "rock":
            return "you are lose the game ... !"
        else:
            return "you are win the game ... !"

choice = choice()
result = selection(choice["player"], choice["computer"])
print(result)

