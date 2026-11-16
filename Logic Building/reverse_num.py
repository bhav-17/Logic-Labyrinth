#Q. Given an Integer n, find the reverse of its digits.

#Solution:

a=int(input("Enter a number:  "))
a=int(str(a)[::-1])
print(a)