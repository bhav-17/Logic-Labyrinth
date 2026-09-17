#Q. Given a positive integer n, find the sum of the first n natural numbers.

#Solution: 

n=int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    sum+=i
    i+=1
print(sum)
