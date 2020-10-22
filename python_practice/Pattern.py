char = '*'
for i in range(1, 4):
    for j in range(1, 7):
        if i == 2 and 1 < j < 6:
            print(' ', end=' ')
        else:
            print(char, end=' ')
    print("")
