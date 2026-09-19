#Q. Given a number n, check whether it is a prime number or not.

#Solution:

num=int(input("Enter a number: "))
s=0
for i in range(1,num+1):
    if num%i==0:
        s+=1
if s==2:
    print("Number is prime ")
else:
    print("Number is not prime")