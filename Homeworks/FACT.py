n=input ()
try:
    n=int(n)
except:
    print (f"{n} is not valid")
    exit (0)
J=1
for item in range(1, n+1):
    J=J*item
print (J)
