# Method to find square root using Newton's Method
def root(num):
    guess_root = num
    precision = 10 ** (-10)

    while abs(num - guess_root * guess_root) > precision:
        guess_root = (guess_root + num / guess_root) / 2
    return guess_root


print("Square Root Using Newton's Method")
number = int(input("Enter a number "))
result = root(number)
print(f"Square Root of {number} by Newton's Method is: {result}")
