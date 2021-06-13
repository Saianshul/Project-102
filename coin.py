import random

print("Coin Flipper")

coin_flip_result = random.randint(1, 2)

if(coin_flip_result == 1):
    print("Heads")
else:
    print("Tails")