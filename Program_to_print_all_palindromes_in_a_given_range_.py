x=int(input())
y=int(input())
for i in range(x,y+1):
    rev=0
    temp=i
    while i>0:
        rem=int(i%10)
        rev=(rev*10)+rem
        i=i//10
    if(rev==temp):
        print(rev,end=" ")