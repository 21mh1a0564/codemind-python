n=int(input())
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
for i in l:
    temp=i
    rev=0
    while i>0:
        rem=int(i%10)
        rev=(rev*10)+rem
        i=i//10
    if(temp==rev):
        print("True")
    else:
        print("False")
    