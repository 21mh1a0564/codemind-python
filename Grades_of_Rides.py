h,sp,spe=map(int,input().split())
if(h>50 and sp>60 and spe>100):
    print("10")
elif(h>50 and sp>60):
    print("9")
elif(sp>60 and spe>100):
    print("8")
elif(h>50 and spe>100):
    print("7")
elif(h>50 or sp>60 or spe>100):
    print("6")
else:
    print("5")