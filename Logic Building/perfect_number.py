#Q. A number is a perfect number if it is equal to the sum of its proper divisors, that is, the sum of its positive divisors excluding the number itself. Find whether a given positive integer n is perfect or not.

#Solution:

num=int(input("Enter a number: "))
divisor_list=[]
sum=0
for i in range(1,num):
    if num%i==0:
        divisor_list.append(i)
for i in divisor_list:
    sum+=i
if sum==num:
    print(True)
else:
    print(False)