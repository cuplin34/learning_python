from random import randint

def game_selector():
    game = input("Which game would you like to play?\nRPS\nnumber guesser\n")
    if game.lower() == "rps":
        play_rps()
    elif game.lower() == "number guesser":
        play_number()
    else: 
        print("Sorry, but please enter a valid game")
        game_selector()


def finish_game():
    question = int(input("------------\nEnter 1 to play another game\nEnter 2 to quit\n"))
    if question == 1:
        # 1 = play a different game
        game_selector()
        #figure out a way for an option to replay the same game without going back to game selector == 2
    else:
        print("Thanks for playing, goodbye")
        quit()

def play_rps():
    ai_score = 0
    pl_score = 0
    rounds_played = int(input("Hello, how many games would you like to play to?\n"))

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
    finish_game()

def play_number():
    game_state = True
    guess_count = 0
    if game_state:
        comp_guess = randint(1,100000)
        player_guess = int(input("Guess a number from 1 to 100000\n"))
        while player_guess != comp_guess:
            if player_guess > comp_guess:
                print("Too high")
            else:   print("Too low")
            guess_count += 1
            player_guess = int(input())
        print(f"Wow you guessed {comp_guess} correctly in {guess_count} guesses")
    finish_game()