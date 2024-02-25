# Function to reverse arr[]
def revArray(arr, d):
    c=(arr[d:])+(arr[:d])
    return c
# Driver function to test above function
arr=[1, 2, 3, 4, 5, 6, 7]
d=2
print(revArray(arr,d))
