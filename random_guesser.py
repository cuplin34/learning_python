from random import randint

game_state = "y"
while game_state == "y":
    comp_guess = randint(1,10)
    player_guess = int(input("Guess a number from 1 to 10\n"))
    while player_guess != comp_guess:
        if player_guess > comp_guess:
            print("Too high")
        else:   print("Too low")
        player_guess = int(input())
        
    print(f"Wow you guessed {comp_guess} correctly")
    game_state = input("Do you want to play again y/n?\n")