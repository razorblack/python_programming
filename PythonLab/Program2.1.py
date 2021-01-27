# Method to perform Matrix Multiplication

def multiplication(X, Y, Z):
    # Logic for Matrix Multiplication
    for i in range(len(X)):
        for j in range(len(Y[0])):
            sum = 0
            for k in range(len(Y)):
                sum += X[i][k] * Y[k][j]
            Z[i][j] = sum
    # Printing multiplied matrix
    printmatrix(Z)

def printmatrix(X):
    for row in X:
        print(row)
    print()

# 3x3 matrix
X = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
# 3x4 matrix
Y = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]
# result is 3x4
result = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

print("First Matrix is:")
printmatrix(X)
print("Second Matrix is:")
printmatrix(Y)
print("Multiplication of First & Second Matrix is:")
multiplication(X, Y, result)