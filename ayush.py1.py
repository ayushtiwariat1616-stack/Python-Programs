#WAP to store 10 name in a list and display name in
# in another list which starts and ends with vowel
c=[]
a=[]
for k in range (10):
    n=input('name=')
    a.append(n)
for i in a:
    if i[0] in 'aeiouAEIUO' and i[-1] in 'aeiouAEIUO':
        c.append(i)
print(c)
