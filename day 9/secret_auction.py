import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

more = True
dict = {}
while more==True:
    name = input('enter your name - ')
    bid = int(input("enter your bid - "))
    dict[name] = bid
    ppl = input("do we have more people? say y or n - ")
    if ppl == 'y':
        clear_console()
    else:
        more = False

max = 0
mkey = ""

for key in dict:
    if dict[key] > max:
        max = dict[key]
        mkey = key

print(f"The winner of the bid is {mkey} with a bid of ${max}")