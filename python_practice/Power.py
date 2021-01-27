def powXY(x, y):
    N = 0
    answer = 0
    while pow(y, N) <= x:
        if x % pow(y, N) == 0:
            answer = N
        N += 1

    return answer



result = powXY(27, 3)
print(result)