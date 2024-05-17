def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1 / n2


def calc(n1,n2,func): #higher oreder functions!
    return func(n1,n2)


print(calc(1,3,add))