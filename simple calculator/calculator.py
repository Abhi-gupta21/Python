def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

process = True
count = 0

while process == True:
    operations = {"+": add,
                  "-": sub,
                  "*": mul,
                  "/": div
                }
    if count == 0:
        num1 = int(input("enter first number - "))
    

    for keys in operations:
        print(keys)

    k = input("select a symbol from above - ")
    if count == 0:
        num2 = int(input("enter second number - "))
    else:
        num = int(input("enter another number - "))

    oper = operations[k]
    if count == 0:
        ans = oper(num1,num2)
    else:
        ans = oper(ans,num)
    i = input("are you done? y or n - ")
    if i == 'n':
        count+=1
    else:
        process = False

print(f"your final answer is {ans}")
