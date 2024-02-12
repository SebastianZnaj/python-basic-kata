from math import sqrt

def Prime(number, itr): # Prime function to check given number prime or not

    if itr == 1:        # base condition
        return True
    if number % itr == 0: # if given number divided by itr or not
        return False
    if Prime(number, itr-1) == False:   # Recursive function Call
        return False

    return True

num = 13

itr = int(sqrt(num)+1)

print(Prime(num,itr))
