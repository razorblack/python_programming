day = input("Enter a day name (Full Name)\n")
day = day.upper()
if day == "MONDAY" or day == "TUESDAY" or day == "WEDNESDAY" or day == "THURSDAY" or day == "FRIDAY":
    print("Weekday \n")
elif day == "SATURDAY" or day == "SUNDAY":
    print("Weekend \n")
else:
    print("Enter a correct input \n")
