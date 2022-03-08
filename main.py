import numpy as np
from tkinter import *
import matplotlib.pyplot as plt

# root = Tk()

# myLabel = Label(root, text="Root test")
# myLabel.pack()

# root.mainloop()

def consoleMultiplyOperator():
    # print("Your resulted matrix was :")
    # for r in result:
    #     print(r)
    newColumn = int(input(f"Your first matrix has {column_b} columns. How many columns should your second matrix have? "))

    print(f"Enter the elements of Second Matrix (column amount for matrix B = {newColumn}): ")

    matrix_b= [[int(input()) for i in range(newColumn)] for i in range(column_b)]
    for n in matrix_b:
        print(n)

    newResult=[[0 for i in range(newColumn)] for i in range(rows_a)]

    for i in range(len(newResult)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                newResult [i][j]+=result[i][k]*matrix_b[k][j]
    print("\nMatrix_a X Matrix_b is: ")
    for r in newResult:
        print(r)
        plt.plot(r, marker="o", markersize=10)
    plt.show()
    # usrInput = input("Do you want to continue?(yes/no) ")
    
    # if(usrInput == "yes".lower() or "y".lower()):
    #     consoleMultiplyOperator()
    # elif (usrInput == "no".lower() or "n".lower()):
    #     exit()
    

def consoleMultiplyOperator1():
    global rows_a
    rows_a = int(input("Enter the Number of rows  for the first matrix: " ))
    column_a = int(input("Enter the Number of Columns for the first matrix: "))

    print("Enter the elements of First Matrix:")
    matrix_a= [[int(input()) for i in range(column_a)] for i in range(rows_a)]

    print("First Matrix is: ")
    for n in matrix_a:
        print(n)
    #the number of columns of first matrix is equal to the number of rows of second matrix
    # column_b = int(input("Enter the Number of Columns for the second matrix: "))
    global column_b
    column_b = 1

    print("Enter the elements of Second Matrix (column amount for matrix B = 1): ")

    matrix_b= [[int(input()) for i in range(column_b)] for i in range(column_a)]
    for n in matrix_b:
        print(n)
        
    global result
    result=[[0 for i in range(column_b)] for i in range(rows_a)]

    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                result [i][j]+=matrix_a[i][k]*matrix_b[k][j]
    print("\nMatrix_a X Matrix_b is: ")
    for r in result:
        print(r)
        plt.plot(r, marker="o", markersize=10, label="matrix 1")
    usrInput = input("Do you want to continue?(yes/no) ")
    
    if(usrInput == "yes".lower() or "y".lower()):
        consoleMultiplyOperator()
    elif (usrInput == "no".lower() or "n".lower()):
        exit()

consoleMultiplyOperator1()
