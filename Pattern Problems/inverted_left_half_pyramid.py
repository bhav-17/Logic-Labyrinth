# Q. Given an integer N, the task is to print N rows of left half pyramid pattern. In left half pattern of N rows, the first row has 1 star, second row has 2 stars and so on till the Nth row which has N stars. All the stars are right aligned.

N=int(input("Enter the number of rows: "))
for i in range(1, N + 1):
    for _ in range(i - 1):
        print(" ", end="")
    for _ in range(N - i + 1):
        print("*", end="")
    print()