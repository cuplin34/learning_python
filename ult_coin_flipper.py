from random import randint

test_case = int(input("How many heads would you like to flip in a row?\n"))
volume = int(input(f"How many times would you like to flip heads {test_case} in a row?\n"))

coin_flip_seq = []
amt_solved = 0
tot_flip = 0
while amt_solved < volume:
    heads_flipped = 0
    i=0
    while heads_flipped < test_case:
        flip = randint(0,1)

        if flip == 0:
            heads_flipped += 1
        else: 
            heads_flipped = 0
        i += 1
        coin_flip_seq.append(i)
    print(f"You flipped {heads_flipped} heads in a row in {i} flips")
    amt_solved += 1

for val in coin_flip_seq:
    tot_flip += val

avg_flip = tot_flip/len(coin_flip_seq)
print(f"Your total average to flip for flipping {test_case} heads in a row {volume} seperate times is: {round(avg_flip, 2)}")
