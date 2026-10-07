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