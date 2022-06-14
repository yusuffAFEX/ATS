l = [1, 2, 3, 4, 5]
u = [6, 7, 8, 9, 10]

l.extend(u)
print(l)
t= []

for i in l:
    if i%2!=0:
        t.append(i)
print(t)
