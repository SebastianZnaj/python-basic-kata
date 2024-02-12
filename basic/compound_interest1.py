# Python3 program to find compound
# interest for given values

def compound_interst(principal, rate, time):

    # Calculate compound interest
    Amount = principal * (pow((1 + rate/ 100),time))
    CI = Amount - principal
    print("Compound interest is", CI)

# Driver Code
compound_interst(10000, 10.25, 5)
