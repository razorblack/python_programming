# Method to perform Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Mid index
        # Finding left and right sub list
        left = arr[:mid]
        right = arr[mid:]

        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left half has been used
                arr[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


size_of_list = int(input("Enter the size of the list \n"))
entered_list = []
for i in range(0, size_of_list):
    entered_list.append(int(input("Enter a element in list \n")))

print("Entered list is:")
print(entered_list)
merge_sort(entered_list)

# Printing list after sorting
print("List after Sorting:")
print(entered_list)
