import random

def CoinFlip(flips):
    for flip in range(flips):
        coin = random.randint(0, 1)
        yield coin

num_of_flips = int(input("Number of flips: "))
for flip in CoinFlip(num_of_flips):
    if flip == 0:
        print("Heads")
    else:
        print("Tails")
