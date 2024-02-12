def sum_of_squares(n):
    if n == 1:
        return 1
    else:
        return n*n + sum_of_squares(n-1)

N = 4
sum_of_squares = sum_of_squares(N)

print("Sum of squares of first", N, "natural numbers", sum_of_squares)
