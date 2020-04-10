x = input()
if x.startswith("ey kheda"):
    A = x.replace("ey kheda", '', 1)
    print(A.lstrip())
else:
    print(x)
