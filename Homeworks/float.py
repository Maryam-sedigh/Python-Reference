N=int(input())
x=[]
for i in range (0,N):
    x.insert(i,float(input()))
print ("Max: {0:.3f}".format(max(x)))
print ("Min: {0:.3f}".format(min(x)))
print ("Avg: {0:.3f}".format(sum(x)/len(x)))