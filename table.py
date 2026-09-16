#Q. Given a number n, we need to print its table with a given limit

#Solution:

num=int(input("Enter a number: "))
limit=int(input("Enter the limit: "))
def table (num,limit):
    for i in range(1,limit+1):
        print(f"{num}x{i}=",num*i)

table(num,limit)