# Python program to Print all Prime numbers in an Interval
# using simple oprimized Sieve of Eratosthenes
# to reduce size of prime array to half and
# reducing iterations.
def bitwiseSieve(srt, n):
    # prime[i] is going to store
    # true if if i*2 + 1 is composite.
    prime = [0] * int(n / 2);

    # 2 in the only even prime, so
    # we can ignore that. Loop
    # starts from 3.
    if srt % 2 == 0:
        srt += 1
    if (srt <= 2):
        srt = 3
    i = srt
    while i * i < n:
        # If i is prime, mark all its
        # multiples as composite
        if (prime[int(i / 2)] == 0):
            j = i * i
            while (j < n):
                prime[int(j / 2)] = 1;
                j += i * 2
        i += 2

    # writing 2 separately
    print(2, end=" ")

    # Printing other primes
    i = 3
    while (i < n):
        if (prime[int(i / 2)] == 0):
            print(i, end=" ")
        i += 2


# Driver code
if __name__=='__main__':
    srt = 1
    end = 10
    bitwiseSieve(srt, end)
