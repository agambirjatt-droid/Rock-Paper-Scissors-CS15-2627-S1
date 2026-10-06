import random

def get_cpu_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_player_choice():
    while True:
        player_choice = input("Enter rock, paper, or scissors: ").strip().lower()
        if player_choice in ["rock", "paper", "scissors"]:
            return player_choice

def check_winner(cpu_choice, player_choice):
    if player_choice == cpu_choice:
            winner = "Tie"
    elif cpu_choice == "rock":
        if player_choice == "paper":
            winner = "PLAYER"
        else:
            winner = "CPU"
    elif cpu_choice == "paper":
        if player_choice == "scissors":
            winner = "PLAYER"
        else:
            winner = "CPU"
    elif player_choice == "paper":
        winner = "CPU"
    else:
        winner = "PLAYER"
    return winner

cpu_choice = get_cpu_choice()
player_choice = get_player_choice()
winner = check_winner(cpu_choice, player_choice)

print(f"CPU chose: {cpu_choice}")
print(f"Player chose: {player_choice}")
print(f"Winner: {winner}")
