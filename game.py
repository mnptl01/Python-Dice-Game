import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll


while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Players has to between 2 and 4")
    else:
        print("Invalid, Try Again!")


max_score = 50
scores = [0 for _ in range(players)]


while max(scores) < max_score:
    for player_idx in range(players):
        print(f"\nPlayer {player_idx+1} turn has started\n")
        current_score = 0
        while True:
            should_roll = input("would you like tp roll (y): ")
            if should_roll != "y":
                break
                
            value = roll()

            if value == 1:
                print("You rolled a 1!")
                current_score = 0
                break 
            else:
                current_score += value 
                print(F"you rolled a {value}!")

            print(F"your current score is {current_score}")
        
        scores[player_idx] += current_score
        print("Your total score is", scores[player_idx])
