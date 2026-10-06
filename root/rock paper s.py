import random
def get_cpu_choice():
    return random.choice(["rock", "paper", "scissors"])
def get_player_choice():
    while True:
        player_choice = input("Enter rock, paper, or scissors: ")
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
def play_round():
    cpu_choice = get_cpu_choice()
    player_choice = get_player_choice()
    winner = check_winner(cpu_choice, player_choice)

    print(f"CPU chose {cpu_choice} Player chose {player_choice}. Result: {winner}")
    return winner
player_wins = 0
cpu_wins = 0
ties = 0
while player_wins < 3 and cpu_wins < 3:
    result = play_round()
    if result == "PLAYER":
        player_wins += 1
    elif result == "CPU":
        cpu_wins += 1
    else:
        ties += 1
    print(f"Score Player: {player_wins} | CPU: {cpu_wins} | Ties: {ties}\n")
if player_wins == 3:
    print("You won")
else:
    print("The computer won")




