# Method to find exponential of any number
def expo(base, power):
    result = 1
    is_power_negative = False
    is_base_negative = False

    # Checking if power is negative or not
    if power < 0:
        is_power_negative = True
        power *= -1

    # Checking if base is negative or not
    if base < 0:
        is_base_negative = True
        base *= -1

    # Logic for exponential
    if base == 0 and power == 0:
        return -1
    elif base != 0 and power == 0:
        return 1
    else:
        for i in range(0, power):
            result *= base

        if is_base_negative == True and is_power_negative == True:
            if power % 2 == 0:
                return 1 / result
            else:
                return -1 / result
        elif is_base_negative == True and is_power_negative == False:
            if power % 2 == 0:
                return result
            else:
                return result * -1
        elif is_base_negative == False and is_power_negative == True:
            return 1 / result
        else:
            return result


print("Exponential of a number:")
# Taking input from user
base_number = int(input("Enter the base number: "))
power_number = int(input("Enter the power to be raised: "))

# Storing Result
result_exponential = expo(base_number, power_number)
if result_exponential == -1:
    print("Exponential can't be calculated")
else:
    print(f"Result of: {base_number} to the power {power_number} is: {result_exponential}")
