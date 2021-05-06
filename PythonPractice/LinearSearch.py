def linearSearch(array, n, x):

    # Going through array (searching)
    for i in range(0, n):
        if array[i] == x:
            return i
    return -1


array = [2, 4, 0, 1, 9]
x = int(input("Enter no to search \n"))
n = len(array)
result = linearSearch(array, n, x)
if result == -1:
    print("Element not found")
else:
    print("Element found at index: ", result)
