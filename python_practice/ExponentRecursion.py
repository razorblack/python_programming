def exponent(x, y, pow):
    if y == 0:
        return pow
    else:
        return exponent(x, y - 1, pow * x)


x = int(input("Enter base number \n"))
y = int(input("Enter power \n"))
result = exponent(x, y, 1)
print(f"Value of {x} to the power {y} is {result}")
