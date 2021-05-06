primeSet = set()
oddSet = set()


def isPrime(i):
    count = 0
    for n in range(2, i):
        if i % n == 0:
            count += 1

    if count > 0:
        return 0
    else:
        return 1


def prime(num):
    count = 0
    i = 1
    while count <= num:
        if isPrime(i) == 1:
            primeSet.add(i)
            i += 1


def isOdd(i):
    if i % 2 != 0:
        return 1
    else:
        return 0


def odd(num):
    i = 1
    count = 0
    while count <= num:
        if isOdd(i) == 1:
            oddSet.add(i)
            i += 1


noOfPrime = int(input("Enter number of elements in prime set "))
noOfOdd = int(input("Enter number of elements in odd set "))
prime(noOfPrime)
print(primeSet)
odd(noOfOdd)
print(oddSet)
