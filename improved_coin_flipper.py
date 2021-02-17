from random import randint

selection = input("Would you like to flip for heads or tails?\n")
test_case = int(input(f"How many {selection} would you like to flip in a row?\n"))
heads_flipped = 0
tails_flipped = 0
i=0
coin_flip_seq = []

#real shotty solution, but cant think of a simpler one with a while loop

if selection == "heads":
    while heads_flipped < test_case:
        flip = randint(0,1)

        if flip == 0:
            heads_flipped += 1
            tails_flipped = 0
        else: 
            tails_flipped += 1
            heads_flipped = 0
        i += 1
        coin_flip_seq.append(flip)
    print(f"You flipped {heads_flipped} heads in a row in {i} flips")
else:
    while tails_flipped < test_case:
        flip = randint(0,1)

        if flip == 0:
            heads_flipped += 1
            tails_flipped = 0
        else: 
            tails_flipped += 1
            heads_flipped = 0
        i += 1
        coin_flip_seq.append(flip)
    print(f"You flipped {tails_flipped} tails in a row in {i} flips")
opt = ""
for val in coin_flip_seq:
    if val == 0:
        opt = opt + "Heads, "
    else: opt = opt + "Tails, "
print(f"Here are your exact coin flips: {opt}")
