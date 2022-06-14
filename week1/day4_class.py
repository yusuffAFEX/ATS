# def func(x=0,y=0):
#     return x+y
# r = {'x':2, 'y':3}
# func(r)

# def func(*y):
#     x = 0
#     sum = 0
#     for i in y:
#         x+=i 
#         sum +=1
#     return x

# print(func(2,3,4,5))
from operator import index


t = {'name':'yusuff', 'age':'3', 'gender':'M'}
for index, value in enumerate(t):
    print(str(index)+' : '+value)