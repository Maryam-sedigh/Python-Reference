x = int(input())
y = int(input())
if y > x:
    print("Wrong order!")
else:
    z = x-y
    A = z % 2
    if A != 0:
        print("Wrong difference!")
    else:
        for number in range(0, x):
            A = " "*y
            inner_sqr_start = ((x-y)/2)-1
            if(inner_sqr_start < number <= inner_sqr_start+y):
                print(" ".join(A.center(x, "*")))
            else:
                print(" ".join("*"*x))
