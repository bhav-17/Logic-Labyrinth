# Q. Given two positive integers num1 and num2. Find the Least Common Multiple (LCM) of a and b.

# Solution:

num1=int(input("Enter a: "))
num2=int(input("Enter b: "))
if num1 < num2:
    hcf = num1
else:
    hcf = num2
while hcf > 0:
    if num1 % hcf == 0 and num2 % hcf == 0:
        break
    hcf = hcf - 1
print("The HCF is:", hcf)