x = input()
A = len(x)
for item in range(0, A-1):
    for char in range(-A, -1, -1):
        print(item, char)
