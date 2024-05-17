i = 2

def ini():
    i = 4
    print(f"val of i inside function = {i}")

ini()

print(f"val of i outside function = {i}")

# when a new var is created in a function its only accessible there

# global scope - 

ph = 10 # global variable! available inside and outside of functions only for functions!
def phh():
    global ph
    ph+=1
phh()
print(ph)