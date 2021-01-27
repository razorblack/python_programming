# Method to perform Insertion Sort
def insertion_sort(arr):
    size = len(arr)
    # Logic for Insertion Sort
    for i in range(1, size):
        value = arr[i]
        j = i -1
        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value

    # Printing list after sorting
    print("List after Sorting:")
    print(arr)


size_of_list = int(input("Enter the size of the list \n"))
entered_list = []
for i in range(0, size_of_list):
    entered_list.append(int(input("Enter a element in list \n")))

print("Entered list is:")
print(entered_list)
insertion_sort(entered_list)