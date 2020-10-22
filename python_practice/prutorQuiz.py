


def add(n):
    if n == 0:
        return 0
    else:
        print(n)
        return n + add(n - 1)


sum1 = add(10)
print(f"Sum = {sum1}")
