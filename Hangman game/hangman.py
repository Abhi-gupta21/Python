import random 

lives = 5
wl = ['ardvark','baboon','camel']

n = random.randint(0,2)
word = wl[n]
guessed = []
for i in range(len(word)):
    guessed.append('-')

print("Welcome to the hangman game. Lets play\n")
while (lives>0) and ('-' in guessed):
    for h in guessed:
        print(f"{h}",end=' ')
    print("\n")
    ch = input("guess a letter - ")
    if ch in word:
        for i in range(len(word)):
            if ch == word[i]:
                guessed[i] = ch
    else:
        lives -= 1

if(lives==0):
    print("sorry you lose")
else:
    print("hurray!! you win!")



