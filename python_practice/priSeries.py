userInput = int(input("Enter a number \n"))
sumOfSeries = 0
for i in range(1, userInput +1):
    sumOfSeries = sumOfSeries + (i**i)/i
print(f"Sum of Series {sumOfSeries}")
