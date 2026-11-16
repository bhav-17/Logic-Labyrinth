# Take multiple numbers Separate them into even and odd lists Count each

#Solution:

num_list =input("Enter numbers separated by comma: ").split(",")
even_list=[]
odd_list=[]
even_count=0
odd_count=0
for i in num_list:
    n_i=int(i)
    if n_i%2==0:
        even_list.append(n_i)
        even_count+=1
    else:
        odd_list.append(n_i)
        odd_count+=1
print(f"Even numbers= {even_list} count= {even_count}")
print(f"Odd numbers= {odd_list} count= {odd_count}")