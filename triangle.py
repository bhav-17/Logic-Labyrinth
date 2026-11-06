nums=input("Enter 3 numbers ").split(",")
while nums[0]+nums[1]>nums[2] or nums[1]+nums[2]>nums[0] or nums[0]+nums[2]>nums[1]:
    if nums[0]==nums[1]==nums[2]:
        print("Equilateral")
        break
    elif nums[0]==nums[1] or nums[0]==nums[2] or nums[1]==nums[2]:
        print("Isoceles")
        break
    else:
        print("Scalene")
        break
else:
    print("none")
