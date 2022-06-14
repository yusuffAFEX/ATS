from math import prod


def factorial(num, x):
    l = list()
    numm= []
    i=1
    while i <num+1:
        numm.append(i)
        r = prod(numm)
        l.append(pow(x, i)/r)
        i +=1
    return sum(l)+1

print(factorial(1, 2))