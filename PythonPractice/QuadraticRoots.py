print("Enter quadratic coefficients \n")
a, b, c = input()
D = (b * b) - (4 * a * c)
root1 = (-b + pow(D, 1 / 2)) / (2 * a)
root2 = (-b + pow(D, 1 / 2)) / (2 * a)
if D == 0:
    print("Equal roots \n")
    print(f"Roots are {root1} and {root2}")
elif D > 0:
    print("Roots are distinct \n")
    print(f"Roots are {root1} and {root2}")
else:
    print("Roots are imaginary \n")
    print(f"Roots are {root1} and {root2}")
