def pattern(N):
    char = '*'
    for i in range(N):
        for k in range(i):
            print(" ", end='')
        for j in range(N):
            print(char, end=' ')
        print("")


pattern(5)