m, s = map(int, input().split())
min=-1
max=-1
for j in range ((10**(m-1)),(10**m)):
    M=0
    x=j
    while x>0:
        M+=x%10
        x//=10
    if M==s:
        min=j
        break
for j in range ((10**(m))-1,(10**(m-1))-1,-1):
    M=0
    x=j
    while x>0:
        M+=x%10
        x//=10
    if M==s:
        max=j
        break
print (min,max)



