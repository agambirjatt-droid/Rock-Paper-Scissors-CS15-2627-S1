
player_wins = 0
cpu_wins = 0
ties = 0

def play_round():
    cpu_choice = get_cpu_choice()
    player_choice = get_player_choice()
    winner = check_winner(cpu_choice,player_choice)
    return winner

while player_wins < 3 and cpu_wins < 3:
    winner = play_round()
    if winner == "PLAYER":
        player_wins += 1
        print(player_wins, "PLAYER wins the game")
    elif winner == "CPU":
        cpu_wins += 1
        print(cpu_wins, "CPU wins the game.")
    else:
        ties += 1
        print(ties, "Both players have chosen the same option, therefore it's a tie")

if player_wins == 3:
    print("Player wins the tournament")
elif cpu_wins == 3:
    print("CPU has won the tournament")





