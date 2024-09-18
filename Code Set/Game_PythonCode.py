"""
Game_PythonCode.py

Author: S. Ganathipan
Location: D:\E21_2nd_Sem\Computing\Python\Final_Project\Code Set V2.5/Game_PythonCode.py
Version: 2.5
Date: 2024-07-24 10:42 PM

Description:
This module defines the game logic for a Rock-Paper-Scissors-Lizard-Spock game.
It includes functions to display available choices, randomly select choices for
the computer, determine round results, and update and display points.
"""

# Import needed modules
import random

# Define the choices available in the game
choices = ["Scissors", "Paper", "Rock", "Lizard", "Spock"]

def choices_available():
    """
    Print the available choices.
    """
    print("\nChoices available:")
    
     # Print each choice along with its corresponding number
    for i, choice in enumerate(choices, start=1):
        print(f"{i}: {choice}")

def computer_choice_selection():
    """
    Randomly select a choice for Player 2 (computer).

    Returns:
    - int: The index of Player 2's choice.
    """
    # Generate a random choice for player 2
    player_choice = random.randint(0, len(choices)-1)
    return player_choice

def show_player_choice(player_choice, player_name):
    """
    Display the choice made by a player.

    Args:
    - player_choice (int): Index of the chosen option.
    - player_name (str): Name of the player.
    """
    # Display the choice made by the player
    if player_choice != 5:
        print(f"{player_name} chose: {choices[player_choice]}")
    else:
        print(f"{player_name} missed the choice")

def round_result(player1_choice, computer_choice):
    """
    Determine the result of a round.

    Args:
    - player1_choice (int): Index of the choice made by player 1.
    - computer_choice (int): Index of the choice made by player 2.

    Returns:
    - int: The winner (1 for Player 1, -1 for Player 2, 0 for a draw).
    """
    if player1_choice !=5:
    # Calculate the winning choices against player 1
        choice1 = (player1_choice + 1) % len(choices)
        choice2 = (player1_choice + 3) % len(choices)

    else:
        return -1 # Player 2 wins

    # Determine the winner of the round
    if player1_choice == computer_choice:
        return 0  # Draw
    elif computer_choice == choice1 or computer_choice == choice2:
        return 1  # Player wins
    else:
        return -1  # Computer wins

def update_points(winner, player1_points, computer_points):
    """
    Update the scores based on the winner of the round.

    Args:
    - winner (int): The winner (1 for Player 1, -1 for Player 2, 0 for a draw).
    - player1_points (int): Score of player 1.
    - computer_points (int): Score of player 2.

    Returns:
    - tuple: Updated scores of both players.
    """
    # Update scores based on the winner
    if winner == 1: 
        print(f"\nPlayer wins the round!\n")
        player1_points += 1
    elif winner == -1:
        print(f"\nComputer wins the round!\n")
        computer_points += 1
    else:
        print(f"\nDraw\n")

    return player1_points, computer_points

def display_final_results(score1, score2):
    """
    Display the final results of the game.

    Args:
    - score1 (int): Final points of Player 1.
    - score2 (int): Final points of Player 2.
    """
    # Display the final scores
    print("\nFinal Results:")
    print("Player score:", score1)
    print("Computer score:", score2)

    # Compare scores to determine the winner
    if score1 > score2:
        print(f"\n \tPlayer Wins the Game!")
        return 1
    elif score1 < score2:
        print(f"\n \tComputer Wins the Game!")
        return -1
    else:
        print(f"\n \tIt's a Draw!")
        return 0
