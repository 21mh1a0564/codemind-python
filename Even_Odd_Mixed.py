n=input()
g=int(n)
f=len(n)
ecount=0
ocount=0
while g>0:
    n=int(g%10)
    if(g%2==0):
        ecount=ecount+1
    elif(g%2!=0):
        ocount=ocount+1
    g=g//10    
if(ecount==f):
    print("Even")
elif(ocount==f):
    print("Odd")
else:
    print("Mixed")