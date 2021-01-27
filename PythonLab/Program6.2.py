# Method to perform Binary Search
def binary_search(list_of_number, no_to_search):
    size = len(list_of_number)
    index = -1
    start = 0
    end = size - 1

    while index == -1 and start <= end:
        mid = (start + end) // 2
        if list_of_number[mid] == no_to_search:
            index = mid
            return index
        elif list_of_number[mid] < no_to_search:
            start = mid + 1
        else:
            end = mid - 1
    return index


size_of_list = int(input("Enter the size of the list \n"))
entered_list = []

# Taking Input of List
for i in range(0, size_of_list):
    entered_list.append(int(input("Enter a element in list \n")))

print("Entered list is:")
print(entered_list)
entered_list.sort()  # Sorting List for Binary Search
print("Sorted List is:")
print(entered_list)
search_number = int(input("Enter a number to search in list \n"))
result = binary_search(entered_list, search_number)
if result == -1:
    print("Search Unsuccessful: Element not found")
else:
    print(f"Search Successful: Element found at index {result}")
