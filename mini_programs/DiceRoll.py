import random
print("Enter 'y' to start rolling dice or 'n' to stop")
res = input("y or n \n")
while res == "y":
    x = random.randint(1, 6)
    if x == 1:
        print("-------")
        print("|     |")
        print("|  o  |")
        print("|     |")
        print("-------")

    if x == 2:
        print("-------")
        print("|  o  |")
        print("|     |")
        print("|  o  |")
        print("-------")

    if x == 3:
        print("-------")
        print("|  o  |")
        print("|  o  |")
        print("|  o  |")
        print("-------")

    if x == 4:
        print("-------")
        print("| o o |")
        print("|     |")
        print("| o o |")
        print("-------")

    if x == 5:
        print("-------")
        print("| o o |")
        print("|  o  |")
        print("| o o |")
        print("-------")

    if x == 6:
        print("-------")
        print("| o o |")
        print("| o o |")
        print("| o o |")
        print("-------")
    res = input("y or n \n")
print("You Successfully rolled the dice")