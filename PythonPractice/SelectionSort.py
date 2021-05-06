def selectionSort(array, size):
    for i in range(size):
        min_index = i

        for j in range(i + 1, size):

            # select the minimum element in each loop
            if array[j] < array[min_index]:
                min_index = j

        # swapping
        (array[i], array[min_index]) = (array[min_index], array[i])


arr = [-2, 45, 0, 11, -9]
size = len(arr)
selectionSort(arr, size)
print("Sorted Array in Ascending Order: ")
print(arr)