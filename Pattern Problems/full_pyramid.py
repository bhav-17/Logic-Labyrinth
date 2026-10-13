# Q. Given an integer N, the task is to print a full pyramid pattern with N rows. In this pattern, each row contains an odd number of stars, ranging from 1 star in the first row to (2 * N - 1) stars in the Nth row. All the stars are center-aligned.

# Solution:

rows=int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()