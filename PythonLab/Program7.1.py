# Method to perform Selection Sort
def selection_sort(arr):
    size = len(arr)
    # Logic for selection sort
    for i in range(0, size - 1):
        small_index = i
        for j in range(i + 1, size):
            if arr[j] < arr[small_index]:
                small_index = j

        temp = arr[i]
        arr[i] = arr[small_index]
        arr[small_index] = temp

    # Printing list after sorting
    print("List after Sorting:")
    print(arr)


size_of_list = int(input("Enter the size of the list \n"))
entered_list = []
for i in range(0, size_of_list):
    entered_list.append(int(input("Enter a element in list \n")))

print("Entered list is:")
print(entered_list)
selection_sort(entered_list)
