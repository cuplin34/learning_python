from random import randint

game_state = "y"
guess_count = 0
while game_state == "y":
    comp_guess = randint(1,100000)
    player_guess = int(input("Guess a number from 1 to 100000\n"))
    while player_guess != comp_guess:
        if player_guess > comp_guess:
            print("Too high")
        else:   print("Too low")
        guess_count += 1
        player_guess = int(input())
        
    print(f"Wow you guessed {comp_guess} correctly in {guess_count} guesses")
    game_state = input("Do you want to play again y/n?\n")
