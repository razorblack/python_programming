userInput = int(input("Enter a number \n"))
factorial = 1
for i in range(1, userInput + 1):
    factorial *= i
print(f"Factorial of {userInput} is {factorial}")
