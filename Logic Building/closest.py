# Q. Given two integers n and m (m != 0). Find the number closest to n and divisible by m. If there is more than one such number, then output the one having maximum absolute value.

#Solution:

n=int(input("Enter the target number: "))
m=int(input("Enter the divisor: "))
q = n // m
cand1 = m * q
cand2 = m * (q + 1) if n * m > 0 else m * (q - 1)
if abs(n - cand1) < abs(n - cand2):
    result = cand1
elif abs(n - cand2) < abs(n - cand1):
    result = cand2
else:
    result = cand1 if abs(cand1) > abs(cand2) else cand2

print(result)