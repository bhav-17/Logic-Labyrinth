# Q. Given an integer N, print N rows of an inverted right half pyramid pattern. In an inverted right half pattern of N rows, the first row has N number of stars, the second row has (N - 1) number of stars, and so on till the Nth row, which has only 1 star.

# Solution:

N=int(input("Enter the number of rows: "))
for i in range(N,0,-1):
    print("*"*i)