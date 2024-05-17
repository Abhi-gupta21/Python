from game_data import data
import random

print("Lets start the game!!")

print()
score = 0
new = random.randint(0,len(data)-1)


print()
game = True
while game==True:
    print(f"your current score - {score}\n")
    n = random.randint(0,len(data)-1)
    for key in data[n]:
        if key == "follower_count":
            continue
        print(f"{key}: {data[n][key]}")

    print()
    for key in data[new]:
        if key == "follower_count":
            continue
        print(f"{key}: {data[new][key]}")


    ch = input(f"enter if you think {data[n]['name']} has more followers than {data[new]['name']}. enter y or n")

    if (data[n]['follower_count'] > data[new]['follower_count']) and (ch == 'y'):
        score += 1
        print("you are right!")
        new = n
    elif (data[n]['follower_count'] < data[new]['follower_count']) and (ch == 'n'):
        score += 1
        print("you are right!")
        new = new
    else:
        game = False
        print("you are wrong")
        print(f"your final score - {score}")


