import string

l = string.ascii_lowercase
t = l[:10]
e = l[16:]
print(t)
print(e)

y= [letter for letter in l if letter in 'aeiou']
z= [letter for letter in l if letter not in 'aeiou']
print(y)
print(z)




