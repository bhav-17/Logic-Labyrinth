#Q. Given two positive integers a and b. Find the Least Common Multiple (LCM) of a and b.

#Solution:

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    greater = num1
else:
    greater = num2
while True:
    if greater % num1 == 0 and greater % num2 == 0:
        break
    greater += 1
print("The LCM is:", greater)