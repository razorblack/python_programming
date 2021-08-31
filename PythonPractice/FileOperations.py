with open("file.txt", 'r+', encoding='utf-8') as f:
    print("Printing the content of the file \n")
    f.seek(0)
    print(f.read())

    print("")
    print("Appending content \n")
    f.write("This is added to this file \n")
    f.write("Through file operations \n")
    f.write("in python. \n")

    print("Printing content after appending\n")
    f.seek(0)
    print(f.read())

    f.close()
