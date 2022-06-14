from tkinter import W


# def draw_pattern():
size = 5
for i in range(size):
    for j in range(i):
        print(" ", end="")
    for j in range(size, i, -1):
        print("*", end="")
    print()

    # t = 5
    # for i in range(6):
    #     print(t * '*')
    #     t-=1
    # print()
    # r = 0
    # for i in range(6):
    #     print(r * '*')
    #     r+=1
    # print()
# p = 5
# for i in range(6):
#     print(p * '*')
#     p+=1


# draw_pattern()

def sort_list(l):
    r= ''
    j= []
    for i in l:
        if r < i:
            r = i
            j.append(i)
    return j

print(sort_list(['c', 'b', 'd', 'a']))