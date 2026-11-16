#Q. Given a non-negative integers n, compute the factorial of the given number. Factorial of n is defined as n * (n -1) * (n - 2) * ... * 1. For n = 0, the factorial is defined as 1.

#Solution:

num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(fact)