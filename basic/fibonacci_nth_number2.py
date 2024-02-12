def nth_fib_multiple(n, k):
    fibonacci = [0, 1]
    counter = 0
    for i in range(2, 10000):
        currnet = fibonacci[i-1] + fibonacci[i-2]
        if currnet % k == 0:
            counter += 1
            if counter == n:
                return i
        fibonacci.append(currnet)

# Example usage
print(nth_fib_multiple(3, 2)) # Output: 9  
