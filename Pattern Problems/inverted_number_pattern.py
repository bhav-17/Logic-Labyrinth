# Q. Print an Inverted Number Pattern
# For n = 3:
# 123
# 12
# 1

n=int(input("Enter the number of rows: "))
for i in range(n+1,1,-1):
    for j in range(1,i):
        print(j,end="")
    print()