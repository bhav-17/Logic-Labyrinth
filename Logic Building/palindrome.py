#Given an integer n, determine whether it is a palindrome number or not. A number is called a palindrome if it reads the same from forward and backward.

# Solution:

num=int(input('Enter a number: '))
rev_num=int(str(num)[::-1])
if num==rev_num:
  print(True)
else:
  print(False)