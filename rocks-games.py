import random

def main():
    show_header()
    
    player = "You"
    ai = "Computer"

    play_game(player, ai)

def show_header():
    print("----------")
    print("Rock Paper Scissors v1")
    print("----------")

def play_game(player_1, player_2):
    rounds = 3
    wins_p1 = 0
    wins_p2 = 0

    rolls = ['rock','paper','scissors']
   
    while wins_p1 < rounds and wins_p2 < rounds:
        roll1 = get_roll(player_1, rolls)
        roll2= random.choice(rolls) 
     
        if not roll1:
            print("Try again!")
            continue
     
        print(f"{player_1} rolls {roll1}")
        print(f"{player_2} rolls {roll2}")

        winner = check_for_winning_throw(player_1, player_2, roll1, roll2) 

        if winner is None:
            print("It was a tie!")
            print()
        else:
            print(f"The winner of this round is {winner}")
            if winner == player_1:
                wins_p1 += 1
            if winner == player_2:
                wins_p2 += 1
            print(f"Standings: {player_1} {wins_p1}  {player_2} {wins_p2}")       
            print() 

    if wins_p1 >= rounds:
        overall_winner = player_1
    else:
        overall_winner = player_2

    print(f"{overall_winner} won the game!")
    
    
def get_roll(player_name, rolls):
    print("Available rolls:")
    for index,  r in enumerate(rolls, start=1):
        print(f"{index}. {r}")

    text= input(f"{player_name}, what is your roll? [rock, paper, scissors]: ")
    selected_index = int(text) - 1 #to convert initial start to 0 for array

    if selected_index < 0 or selected_index >= len(rolls):
        print(f"Sorry {player_name}, {text} is not a valid play!")
        return None 

    return rolls[selected_index]

def check_for_winning_throw(player_1, player_2, roll1, roll2):
    # Test for a winner
    # Rock
    # Rock -> tie
    # Paper -> lose
    # Scissors -> win
    # Paper
    # Paper -> tie
    # Scissors -> lose
    # Rock -> win
    # Scissors
    # Scissors -> tie
    # Rock -> lose
    # Paper -> win

    winner = None

    if roll1 == roll2:
        print("The play was tied!")
    elif roll1 == 'rock':
        if roll2 == 'paper':
            winner = player_2
        elif roll2 == 'scissors':
            winner = player_1
    elif roll1 == 'paper':
        if roll2 == 'scissors':
            winner = player_2
        elif roll2 == 'rock':
            winner = player_1
    elif roll1 == 'scissors':
        if roll2 == 'rock':
            winner = player_2
        elif roll2 == 'paper':
            winner = player_1
    return winner


if __name__ == '__main__':
    main()
