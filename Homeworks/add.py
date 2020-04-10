X=input ()
try:
    X=int(X)
except:
    print (f"{X} is not valid")
    exit (0)
Y=input()
try:
    Y=int(Y)
except:
    print (f"{Y} is not valid")
    exit (0)
print (X+Y)
