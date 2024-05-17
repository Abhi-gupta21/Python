import random
import sys

def over21(n):
    if n > 21:
        return 0
    else:
        return 1
    
def cardgen():
    cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def sumlist(list):
    sum = 0
    for i in list:
        sum+=i
    return sum

game = input("do you want to play a black jack game? y or n ")

if game == 'y':
    player = []
    comp = []
    player.append(cardgen())
    player.append(cardgen())
    comp.append(cardgen())
    comp.append(cardgen())
    print(f"players cards are - {player}\nplayers sum = {sumlist(player)}")
    print(f"one of the dealers card - {comp[0]}")    
    hit = input("would you wish to hit? y or n ")

    while hit == 'y':
        player.append(cardgen())
        print(f"players cards are - {player}\nplayers sum = {sumlist(player)}")
        if sumlist(player) > 21:
            print(f"your cards are - {player} which sums to {sumlist(player)}, therefore you lose")
            sys.exit()
        hit = input("would you wish to hit again? y or n ")
    print(f"dealers cards - {comp}, sum - {sumlist(comp)}")
    if sumlist(comp) < 17:
        comp.append(cardgen())
        print(f"dealers cards - {comp}, sum - {sumlist(comp)}")


    if (sumlist(comp) > 21 and sumlist(player) > 21) or (sumlist(comp) == sumlist(player)):
        print(f"players cards - {player}, sum = {sumlist(player)}\ndealers cards - {comp}, sum = {sumlist(comp)}\nits a draw!")
    elif sumlist(comp) > 21:
        print(f"players cards - {player}, sum = {sumlist(player)} \ndealers cards - {comp}, sum = {sumlist(comp)}\nyou win!!")
    elif sumlist(player) > 21:
        print(f"players cards - {player}, sum = {sumlist(player)} \ndealers cards - {comp}, sum = {sumlist(comp)}\nyou lose!!")
    else:
        pdiff = 21 - sumlist(player)
        ddiff = 21 - sumlist(comp)
        if pdiff < ddiff:
            print(f"players cards - {player}, sum = {sumlist(player)} \ndealers cards - {comp}, sum = {sumlist(comp)}\nyou win!!")
        else:
            print(f"players cards - {player}, sum = {sumlist(player)} \ndealers cards - {comp}, sum = {sumlist(comp)}\nyou lose!!")
