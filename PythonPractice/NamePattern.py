name = "Avinash"
userInput = int(input("Enter no. of times to be printed \n"))

for i in range(userInput):
    if i % 2 == 0:
        print(name)
    else:
        print(f"  {name}")
