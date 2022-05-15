n=int(input())
fact=1
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
for i in l:
    for j in range(i,1,-1):
        fact=fact*j
    print(fact)
    fact=1