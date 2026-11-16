# Q. You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's. Increment the large integer by one and return the resulting array of digits.

#Solution:

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in digits:
         position=int(digits[-1])
         if position<9:
            add=position+1
            digits[-1]=add
            print(digits)
         elif position==9:
            for i in digits:
                add=position+1
                digits