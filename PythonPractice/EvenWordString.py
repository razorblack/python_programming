def even_length_word(sentence):
    splitlist = sentence.split()
    for i in range(0, len(splitlist)):
        word = splitlist[i]
        if len(word) % 2 == 0:
            print(word)


string = input("Enter a sentence ")
even_length_word(string)
