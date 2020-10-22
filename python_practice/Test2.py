string = input()
length = len(string)
countVow = 0
countCons = 0
countBlank = 0
string = string.lower()
for i in range(0,length):
    char = string[i]
    if char == " ":
        countBlank +=1
    elif char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        countVow += 1
    else:
        countCons += 1
print(countCons)
print(countVow)
print(countBlank)
