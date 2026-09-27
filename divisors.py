# Q. Given a positive integer n, return all the divisors of n in the ascending order.

#Solution: 

num=int(input("Enter a number: "))
divisors=[]
for i in range(1,num+1):
    if num%i==0:
        divisors.append(i)
print(divisors)