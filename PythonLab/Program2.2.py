# Method to find Greatest Common Divisor(GCD) of entered number

def gcd(num1, num2):
    gcd_result = 1
    minimum = min(num1, num2)
    for i in range(2, minimum + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcd_result = i
    return gcd_result


print("Greatest Common Divisor")
first_number = int(input("Enter first number \n"))
second_number = int(input("Enter second number \n"))
print(f"Greatest Common Divisor of {first_number} and {second_number} is:")
result = gcd(first_number, second_number)
print(result)
