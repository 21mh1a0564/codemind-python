n=int(input())
f=n//2
sum=0
for i in range(1,f+1):
    r=n%i
    if(r==0):
        sum=sum+i
if(n==sum):
    print("True")
else:
    print("False")
    