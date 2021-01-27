# Method to print prime numbers in user entered range
def prime_in_range(n):
    for i in range(2, n + 1):
        if prime(i) == True:
            print(i, end=" ")
    return


# Method to check for prime number
def prime(num):
    factor_count = 2  # 1 and Number itself are factors
    for i in range(2, num):
        if num % i == 0:
            factor_count += 1

    if factor_count == 2:
        return 1
    else:
        return 0


prime_range = int(input("Enter a range to print prime number \n"))
prime_in_range(prime_range)
