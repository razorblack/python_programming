userInput = int(input("Enter a number to check for prime \n"))
count = 0  # To count no. of factors of user input number
for i in range(2, userInput):
    if userInput % i == 0:
        count += 1
if count > 0:
    print(f"{userInput} is composite number")
else:
    print(f"{userInput} is a prime number")
