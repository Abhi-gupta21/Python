import pandas

# Primary Fur Color

no_black = 0
no_cinnamon = 0
no_gray = 0

data = pandas.read_csv("day 25 pandas/squirrel_data.csv")

color = data["Primary Fur Color"].to_list()

print(color)

for c in color:
    if c == "Black":
        no_black = no_black + 1
    elif c == "Cinnamon":
        no_cinnamon = no_cinnamon + 1
    elif c == "Gray":
        no_gray = no_gray + 1

my_dict = {"color" : ["Black", "Cinnamon", "Gray"],
           "number of squirrels" : [no_black, no_cinnamon, no_gray]}

my_data = pandas.DataFrame(my_dict)
my_data.to_csv("day 25 pandas/my_squirrel_data.csv")


# or 

# grey = len(data[data["Primary Fur Color"] == "Gray"])