from random import randint

# 0 = rock, 1 = paper, 2 = scissors
comp_move = randint(0,2)
player_move = input("Whats your move? ")
if player_move[0].lower() == "r":
    player_move = 0
elif player_move[0].lower() == "p":
    player_move = 1
else:
    player_move = 2

if player_move == comp_move:
    print("Draw!")
elif player_move > comp_move or (comp_move == 2 and player_move == 0):
    print("Player wins!!!")
else:
    print("AI wins!?!?!?")
