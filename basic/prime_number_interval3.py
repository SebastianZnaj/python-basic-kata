# Python program to find the prime numbers
# between a given interval using Sive of Eratosthenes
import math

def SieveOfEratosthenes(str,n):
    # Create a boolean array "prime[str to n]" and
    # initialize all enteries it as true. A value in
    # prime[i] will finally be false if i is Not a prime,
    # else true.
    prime = [True for i in range(n + 2 - str)]
    prime[0] = False
    prime[1] = False

    for p in range(str, int(math.sqrt(n))+1):
        # If prime[p] is not changed, then it is a prime
        if prime[p] == True:
            # Update all multiples of p greater than or
            # equal to the square of it numbers which are
            # multiple of p and are less than p^2 are
            # already been marked.
            for i in range(p*p, n+1, p):
                prime[i] = False

    # Print all prime numbers 
    for p in range(str, n+1):
        if prime[p]:
            print(p, end=" ")

# Driver Code
if __name__ == "__main__":
    str = 1
    end = 10
    SieveOfEratosthenes(str, end)
