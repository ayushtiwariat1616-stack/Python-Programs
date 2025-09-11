#pattern printing by fixing t alphabets in each line
s='scjvhh sdjhhvfdsh shvh dsdhcuswhw hg kjdsvhcb ndsdsjawHf ggf wegkjbsdag b'
f=''
t=9
o=t
d=s.split()
p=0
for k in d:
    f+=k
v=len(f)//t
g=math.ceil(len(f)/t)
if v==g:
    for k in range(v):
        y=''
        for i in range(p,t):
            y+=f[i]
        print(y)
        t+=o
        p+=o
if g>v:
    a=len(f)%t
    e=t-a
    w=f
    for r in range(e):
        w+=' '
    for k in range(v+1):
        y=''
        for i in range(p,t):
            y+=w[i]
        print(y)
        t+=o
        p+=o    

    





