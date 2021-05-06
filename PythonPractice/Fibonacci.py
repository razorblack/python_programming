def fibonacci(a, b, n, l):
    if n == 0:
        print("Done")
    else:
        c = a + b
        l.append(c)
        n -= 1
        fibonacci(b, c, n)


l = [0, 1]
userInput = int(input("Enter no.\n"))
fibonacci(0, 1, userInput, l)
