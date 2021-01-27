def max_in_list(list_of_number):
    max = list_of_number[0]
    for i in range(1, len(list_of_number)):
        if list_of_number[i] > max:
            max = list_of_number[i]

    print(f"Maximum element of the list is: {max}")
    return


size_of_list = int(input("Enter the size of the list \n"));
entered_list = []
for i in range(0, size_of_list):
    entered_list.append(int(input("Enter a element in list \n")))
print("Entered list is:")
print(entered_list)
max_in_list(entered_list)