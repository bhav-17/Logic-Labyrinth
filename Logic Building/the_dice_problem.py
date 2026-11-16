#Q. You are given a cubic dice with 6 faces. All the individual faces have a number printed on them. The numbers are in the range of 1 to 6, like any ordinary dice. You will be provided with a face of this cube, your task is to guess the number on the opposite face of the cube.

#Solution:

f = int(input('Enter the number on face: '))
list_1 = [1, 2, 3]
list_2 = [6, 5, 4]

if f in list_1:
    print(list_2[list_1.index(f)])
elif f in list_2:
    print(list_1[list_2.index(f)])
else:
    print("Invalid die face")