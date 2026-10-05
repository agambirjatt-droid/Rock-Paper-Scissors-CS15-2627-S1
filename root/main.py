import random


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
  else:
    if player_choice == "rock":
      winner = "PLAYER"
    else:
      winner = "CPU"

  return winner

