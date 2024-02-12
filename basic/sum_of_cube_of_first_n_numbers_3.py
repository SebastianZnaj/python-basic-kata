# Efficient Python program to find sum of cubes
# of first n naturaal numbers that avoids
# overflow if result is going to be with in
# limits.

# Returns the sum of series
def sumOfSeries(n):
    x = 0
    if n % 2 == 0:
        x = (n / 2) * (n + 1)
    else:
        x = ((n +1) / 2 ) * n

    return (int)(x * x)

# Driver Function
n = 5
m = 6
print(sumOfSeries(n))
print(sumOfSeries(m))
