# Python3 program to check
# whether the given number is amstrong or not
# without using power finction

n = 153     # or n=int(input()) -> taking input from user
s = n       # assiging input value to the s variable
b = len(str(n))
sum1 = 0
while n != 0:
    r = n % 10
    sum1 = sum1 + (r**b)
    n = n // 10
if s == sum1:
    print("The give number ", s, " is amstrong number")
else:
    print("The give number ", s, " is not amstrong number")

# This code is awersome
