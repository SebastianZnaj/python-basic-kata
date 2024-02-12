# Python program to find the
# maximum of two numbers

def maximum(a, b):

    if a >= b:
        return a
    else:
        return b

# Driver code
a = input("Fist number: ")
b = input("Second number: ")
print(maximum(a,b))
