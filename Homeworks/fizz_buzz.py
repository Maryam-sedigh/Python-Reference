def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "fizz_buzz"
    if input % 5 == 0:
        return "buzz"
    if input % 3 == 0:
        return "fizz"
    return input


print(fizz_buzz(9))
