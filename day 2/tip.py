print("welcome to tip calculator.")
bill = float(input("what was the total bill? $"))
n = int(input("how many people to split the bill? "))
tipp = int(input("what percentage tip would you like to give? "))
perp = ((bill/100)*tipp + bill)/n #perp = per person
#perp = round(perp,2)
perp = "{:.2f}".format(perp)
print(f"Each person should pay: ${perp}")

# you can use the type() function to know the data type of a variable.