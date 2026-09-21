#Q. Given a number n, find the sum of its digits.
#Solution:

num=input("Enter your number: ")
sum=0
for i in num:
     sum+=int(i)
if sum<10:
   print(sum)
elif sum>=10:
   new_num=str(sum)
   sum=0
   for j in new_num:
       sum+=int(j)
   print(sum)
       


    
      