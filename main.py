import numpy as np

p = int(input("Matrix #rows:"))
q = int(input("Matrix #columns:"))
n = int(input("#Columns for A / #rows for B:"))

print("Enter the elements for matrix A :")
A = [[int(input()) for i in range(n)] for j in range(p)]
print("Matrix A:")
for i in range(p):
    for j in range(n):
        print(format(A[i][j], "<3"), end="")
    print()


print("Enter the elements for matrix B :")
B = [[int(input()) for i in range(q)] for j in range(n)]
print("Matrix B:")
for i in range(n):
    for j in range(q):
        print(format(B[i][j], "<3"), end="")
    print()

result = [[0 for i in range(q)] for j in range(p)]

for i in range(p):
    for j in range(q):
        for k in range(n):
            result[i][j] = result[i][j] + A[i][k] * A[k][j]

print("Result:")
for i in range(p):
    for j in range(q):
        print(format(result[i][j], "<3"), end="")
    print()
