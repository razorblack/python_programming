# Method to find most frequent word
def most_frequent(fname):
    count = 0  # count of a specific word
    maxcount = 0  # maximum among the count of each words
    l = []  # list to store the words with maximum count
    with open(fname, 'r') as f:
        contents = f.read()
        words = contents.split()

        # Logic for max occurring word
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] == words[j]:
                    count += 1
            if count >= maxcount:
                l.clear()
                l.append(words[i])
                maxcount = count

            count = 0

    # Printing the list of most occurring word
    print(l)


file = input("Enter the file name\n")
print("Most frequent word in the text file is:")
most_frequent(file)
