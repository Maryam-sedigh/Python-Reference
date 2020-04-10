A = int(input())
Z = A
b = 0
while A != 0:
    b += A % 10
    A //= 10
counter = 0
while counter < b:
    Z += 1
    isPrime = True
    for i in range(2, Z):
        if Z % i == 0:
            isPrime = False
    if isPrime == True:
        counter += 1
print(Z)
