from random import randint

test_case = int(input("How many heads would you like to flip in a row?\n"))
heads_flipped = 0
i=0
coin_flip_seq = []
while heads_flipped < test_case:
    flip = randint(0,1)

    if flip == 0:
        heads_flipped += 1
    else: 
        heads_flipped = 0
    i += 1
    coin_flip_seq.append(flip)

opt = ""
for val in coin_flip_seq:
    if val == 0:
        opt = opt + "Heads, "
    else: opt = opt + "Tails, "
print(f"You flipped {heads_flipped} heads in a row in {i} flips")
print(f"Here are your exact coin flips: {opt}")
