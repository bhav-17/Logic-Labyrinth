# Q. Given an integer N, print a right half pyramid star pattern with N rows. The first row has 1 star, the second row has 2 stars, and each next row has one more star than the previous row. The Nth row has N stars, and all stars are left aligned.

# Solution:

N=int(input("Enter the number of rows: "))
for i in range(1,N+1):
    print("*"*i)