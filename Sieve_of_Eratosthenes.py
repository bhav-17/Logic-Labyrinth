# Q. Given a number n, find all prime numbers less than or equal to n.

# Solution:

# Given a number n, find all prime numbers less than or equal to n.

n=int(input("Enter a number: "))
prime=[]
for i in range(1,n+1):
  flage = False
  for j in range(2,i):
      if i%j==0:
        flage=True
        break
  if(flage==False and i!=1):
    prime.append(i)

print(prime)