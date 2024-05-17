fruits = ['apple','banana']
vegie = ['tomato','peppers']

print(fruits[0])
print("")

for f in fruits:
    print(f)

print("")

edi = fruits + vegie

for e in edi:
    print(e)

print()
print(fruits[-1])

fruits.append('pineapple')

print()

for f in fruits:
    print(f)

# go to documentation for more functions on list.

print(len(fruits))
print(fruits[3-1])
print()
print()


# lists in a list -

veg = [fruits,vegie]

print(veg)

print()

print(veg[1][1])
