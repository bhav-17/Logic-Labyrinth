# Q. Given a positive integer n, we have to find the sum of squares of first n natural numbers. 

#Solution: 

n=int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    sq=i**2
    sum+=sq
    i+=1
print(sum)