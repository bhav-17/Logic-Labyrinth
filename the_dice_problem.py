f = int(input('Enter the number on face: '))
list_1 = [1, 2, 3]
list_2 = [6, 5, 4]

if f in list_1:
    print(list_2[list_1.index(f)])
elif f in list_2:
    print(list_1[list_2.index(f)])
else:
    print("Invalid die face")
# if f==list_1[0]:
#   print(list_2[0])
# elif f==list_1[1]:
#   print(list_2[1])
# elif f==list_1[2]:
#   print(list_2[2])
# else:
#   print("Out of range!")

#Sample Concept: f ka value i ka konsa index se match krra h uska corresponding index j ka print kra do