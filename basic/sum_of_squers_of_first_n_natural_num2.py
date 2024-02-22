# Python3 Program to
# find sum of square
# of first n natual
# numbers

# Return the sum of
# square of first n
# natual numbers

def squaresum(n):
  return (n * (n + 1) * (2 * n + 1)) // 6

# Driver Program
n = 4
m = 5
print(squaresum(n))
print(squaresum(m))
