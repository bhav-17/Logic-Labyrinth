#Given a number x, check if the given number is Armstrong's number or not. A positive integer of n digits is called an Armstrong number of order n (order is the number of digits) if
# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....
# Here a, b, c and d are digits of input number abcd.....

#Solution:

num=input("Enter a number: ")
sum=0
for i in num:
    if sum==int(i)**len(num):
        print("The number is an Armstrong number")
        break
    else:
        print("The number is not an Armstrong number")