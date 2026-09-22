# Q. Given a positive integer num, return true if num is a perfect square or false otherwise.
# You must not use any built-in library function, such as sqrt.

#Solution:

num=int(input("Enter a number "))
root=int(num**0.5)
i=1
for i in range(1,root):
    i+=1
    if i**2==num:
        print("True")
        break
else:
    print("False")
    