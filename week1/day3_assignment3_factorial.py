def positive_integer_factorial(positiveInteger):
    if positiveInteger > 0:
        if positiveInteger == 1:
            return 1
        else:
            return positiveInteger  * (positive_integer_factorial(positiveInteger-1))
    else:
        return "Enter positive Integer"

print(positive_integer_factorial(1))


def facb(terms):
    constant = 1
    for i in range(1, terms+1):
        constant += 1/positive_integer_factorial(i)
    return constant

print(facb(1)) 