"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare
them, print out a message of congratulations to the winner, and ask if the players want to start a
new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""

game = True

while game:
    player_input = int(input("One or two players: "))
    if player_input == 1:
        print("One player")
        game = False
    elif player_input == 2:
        print("Two players")
        game = False
    else:
        print("Please enter one or two players")
        continue

