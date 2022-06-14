# def positive_integer_factorial(positiveInteger):
#     if positiveInteger > 0:
#         if positiveInteger == 1:
#             return 1
#         else:
#             t=0
#             while positiveInteger != 1:
#                 r = (1/(positiveInteger  * (positive_integer_factorial(positiveInteger-1))))
#                 t +=r
#                 positiveInteger -=1
#             return t+2
            

#     else:
#         return "Enter positive Integer"

# print(positive_integer_factorial(1))


# def reverse(word):
#     word = list(word)
#     for i in word:
#         if word.count(i) == 1:
#             return i 
#     return False

# print(reverse([1, 1, 1, 3, 3, 3]))


from math import prod


def prodt(number_list):
    sum_up=1
    for i in number_list:
        sum_up*=i
    return sum_up

# def factorial(num):
#     l = list()
#     numm= []
#     i=1
#     while i <num+1:
#         numm.append(i)
#         r = prodt(numm)
#         print(r)
#         l.append(1/r)
#         i +=1
#     return sum(l)+1

# print(factorial(3))







def fac(n):
    l = []
    w= []
    for i in range(1, n+1):
        l.append(i)
        r = prod(l)
        w.append(1/r)
    return(sum(w)+1)
print(fac(4))