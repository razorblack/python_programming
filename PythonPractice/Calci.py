import calcaulatorModule

x = int(input("Enter a no:  "))
y = int(input("Enter a no:  "))

add_res = calcaulatorModule.add(x, y)
sub_res = calcaulatorModule.subtract(x, y)
multi_res = calcaulatorModule.multiply(x, y)
div_res = calcaulatorModule.divide(x, y)


print(add_res)
print(sub_res)
print(multi_res)
print(div_res)