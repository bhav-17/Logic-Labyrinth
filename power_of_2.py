#Q. Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.

#Solution:

n=int(input("Enter a number: "))
for i in range(0,n+1):
    if 2**i==n:
        print(True)
        break
else:
    print(False)

# Better time complexity 
    class Solution:
        def isPowerOfTwo(self, n: int) -> bool:
            if n <= 0:
                return False

            while n % 2 == 0:
                n //= 2
            return n == 1