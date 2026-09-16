#Q. Given a number n, check whether it is even or odd. Return true for even and false for odd.

num=int(input("Enter a number: "))
def check(num):
    if num % 2 == 0:
        return True
    else:
        return (False)

print(check(num))