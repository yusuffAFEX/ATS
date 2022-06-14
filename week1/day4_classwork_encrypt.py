import string
def encrypt():
    spec_char = {
        'a':'#',
        'e':'&',
        'i':'%',
        'o':'$',
        'u':'*'
    }

    f = []
    s = input('Type any string: ')
    # for key, value in spec_char.items():
    for i in s:
        f.append(i)
            # if key == i:
            #     i[index] = value
    for key, value in spec_char.items():
        for i, j in enumerate(f):
            if j == key:
                f[i] = value
            if j == value:
                f[i]= '|'+value
            if j != key:
                t = str(j).capitalize()
                #f[i] = t
        
    print("".join(f))









encrypt()




# s = ['b', 'o']
# t=s[0].capitalize()
# s[0]=t
# print(s)