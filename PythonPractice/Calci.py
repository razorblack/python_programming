import CalculatorModule

x = int(input("Enter a no:  "))
y = int(input("Enter a no:  "))

add_res = CalculatorModule.add(x, y)
sub_res = CalculatorModule.subtract(x, y)
multi_res = CalculatorModule.multiply(x, y)
div_res = CalculatorModule.divide(x, y)

print(add_res)
print(sub_res)
print(multi_res)
print(div_res)
