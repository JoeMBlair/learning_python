import random
coins_flipped = []

def get_streak_count(coin_flips):
    last_coin = ''
    streak_count = 0
    flip_streak = 0

    for i in range(len(coin_flips)):
        if last_coin != coin_flips[i]:
            streak_count = 0
        elif last_coin == '':
            streak_count += 1
        else:
            streak_count += 1
        
        if streak_count == 6:
            flip_streak += 1

        last_coin = coin_flips[i]
    
    print('Chance of streak: {}'.format(flip_streak / 100))


def generate_coin_flips(amount):
    coin_flips = []
    for i in range(amount):
        if random.randint(0, 1) == 0:
            coin_flips.append('Heads')
        else:
            coin_flips.append('Tails')
    return coin_flips

coins_flipped = generate_coin_flips(10000)
get_streak_count(coins_flipped)

