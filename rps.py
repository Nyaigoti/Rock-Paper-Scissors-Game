import sys
import random
from enum import Enum

def rps(name='Player One'):
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal computer_wins
        
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3
            

        player_choice = input(f"Lets play rock paper scissors,{name}. Please enter: \n1 for rock \n2 for paper \n3 for scissors \nYou choose? ")
        
        if player_choice not in ["1", "2", "3"]:
            print(f"{name},please choose either 1, 2, or 3.")
            return play_rps()
        
        player = int(player_choice)    
        computer_choice = random.choice([1,2,3])
        computer = int(computer_choice)

        print("")
        print(f"{name} chose {str(RPS(player)).replace('RPS.', '')}.")
        print(f"Computer chose {str(RPS(computer)).replace('RPS.', '')}.")
        print("")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal computer_wins
        
            if (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
                player_wins += 1
                return f"{name}, you win!"
            elif player == computer:
                return  'It\'s a tie'
            else:
                computer_wins += 1
                return "Computer wins!\nSorry, {name}..."
            
        game_result = decide_winner(player, computer)    
        print(game_result)
        
        nonlocal game_count
        game_count += 1
        
        print(f"\nGame count: {game_count}")
        print(f"{name}'s wins: {player_wins}")
        print(f"Computer wins: {computer_wins}")
            
        
        while True:
            print(f"\nDo you want to play again?")
            playagain = input("\nY for Yes \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break
            
        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\nThank you for playing")
            sys.exit(f"Bye,{name}")
            
    return play_rps
        


if __name__ == '__main__':
    import argparse

    parse = argparse.ArgumentParser(
        description= "Provides a personalized gaming experience"
    )

    parse.add_argument(
        "-n", "--name", metavar="name",
        required= True, help="The name of the person playing the game"
    )

    args = parse.parse_args()   
    
    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()


