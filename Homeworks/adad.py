B=int(input())
z=B
c=0
while B>0:
    c*=10
    c+=B%10
    B=int(B/10)
while c!=0:
    x=c%10
    b=0
    for i in range(0,x):
        b+=x*(10**i)
    if b!=0:
        print (f"{x}: {b}")
    else:
        print("0: ")
    c=int(c/10)
while z%10==0:
    print ("0: ")
    z=int(z/10)

    
