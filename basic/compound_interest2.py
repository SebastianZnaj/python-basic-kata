# Python 3 program to find compound
# interest for input taking from user.

def compound_interest(principal, rate, time):

    # Calculate compound interest
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print("Compound interest is", CI)

# Driver Code
# Taking input from user.
principal = int(input("Enter the principal amount: "))
rate = int(input("Enter rate of interest : "))
time = int(input("Enter time in years : "))

# Function Call
compound_interest(principal, rate, time)

