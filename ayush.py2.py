#WAP to make a dict from given list where key is
#index and value is length of nested list
a=[[6,8,9],[10,12,],[16,17,18,20,25]]
b={}
for k in a:
    m=a.index(k)
    for i in k:
        n=len(k)
        b[m]=n
print(b)
