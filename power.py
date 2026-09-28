#Q. Given two positive numbers x and y, check if y is a power of x or not.

#Solution:

x=int(input("Enter a number: "))
y=int(input("Enter target: "))
for i in range(0,y):
    if x**i==y:
        print(True)
        break
else:
    print(False)