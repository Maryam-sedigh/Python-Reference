#A = input()
#B = int(A, 2)
#print(format(B, 'x'))
""" A=int(input())
i=0
while A!=0:
    B=A%10
    A//=10
    if (B==0 or B==1):
        i+=1
print(i) """
A=int(input())
G=A
i=0
while A>0:
    B=A
    while B!=0:
        C=B%10        
        if not (C==0 or C==1):
            i+=1
            break
        B//=10
    A-=1
j=G-i
print (j)