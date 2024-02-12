# Python program to find simple interest
# principal amount, time and 
# rate of interest taken from user.

def simple_interest(p,t, r):
#    print('\nThe principal is ', p)
#    print('The time period is ', t)
#    print('The rate of interst is ', r)

    si = (p * t * r)/100

    print('\nThe Simple Interest is', si)

# Driver Code

P = int(input("Enter the principal amount :"))
T = int(input("Enter the time period :"))
R = int(input("Enter the rate of interest :"))
simple_interest(P,T,R)
