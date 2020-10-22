def fibonacci(a, b, n):
    if n == 0:
        print("Done")
    else:
        c = a + b
        print(c)
        n -= 1
        fibonacci(b, c, n)


a = 0
b = 1
print(a)
print(b)
userInput = int(input("Enter no. of Fibonacci terms to be printed \n"))
fibonacci(a, b, userInput - 2)
