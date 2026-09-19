#Q. Given two positive integers a and b. Find the Least Common Multiple (LCM) of a and b.

#Solution:

a=int(input("Enter a: "))
b=int(input("Enter b: "))
if a%b==0 and a>b:
    print(a)
elif b%a==0 and b>a:
    print(b)
else:
    print(a*b)