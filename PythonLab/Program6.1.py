# Method to perform Linear Search
def linear_search(list_of_number, no_to_search):
    size = len(list_of_number)
    for i in range(0, size):
        if list_of_number[i] == no_to_search:
            print(f"Search Successful: Element found at index {i}")
            return

    print("Search Unsuccessful: Element Not Found")
    return


size_of_list = int(input("Enter the size of the list \n"))
entered_list = []
for i in range(0, size_of_list):
    entered_list.append(int(input("Enter a element in list \n")))
print("Entered list is:")
print(entered_list)
search_number = int(input("Enter a number to search in list \n"))
linear_search(entered_list, search_number)
