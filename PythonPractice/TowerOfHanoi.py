# Method to solve tower of hanoi problem
def toh(n, a, b, c):
    if n == 1:
        print(f"Move from {a} to {c}")
        return
    toh(n - 1, a, c, b)
    print(f"Move from {a} to {c}")
    toh(n - 1, b, a, c)


print("Tower of Hanoi")
disks = int(input("Enter no. of disks\n"))
toh(disks, 'A', 'B', 'C')
