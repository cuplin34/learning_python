from random import randint

ai_score = 0
pl_score = 0
# 0 = rock, 1 = paper, 2 = scissors
rounds_played = int(input("Hello how many games would you like to play to?\n"))

while pl_score < rounds_played and ai_score < rounds_played:
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
        pl_score += 1
    else:
        print("AI wins!?!?!?")
        ai_score += 1
    print(f"Score- Player: {pl_score} to AI: {ai_score}")