dice1, dice2, dice3 = map(int, input().split())
if dice1 == dice2 == dice3:
    price = 10000 + dice1 * 1000
elif dice1 == dice2 or dice1 == dice3:
    price = 1000 + dice1 * 100
elif dice2 == dice3:
    price = 1000 + dice2 * 100
elif dice1 != dice2 != dice3:
    if dice1 > dice2 and dice1 > dice3:
        price = dice1 * 100
    elif dice2 > dice3 and dice2 > dice1:
        price = dice2 * 100
    else:
        price = dice3 * 100

print(price)