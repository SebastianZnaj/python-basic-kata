# Python program for reversal algorithm of array rotation

# Function to reverse arr[] from index start to end
def revArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end - 1

# Function to left rotate arr[] of size n by d
def leftRotate(arr, d):
    n = len(arr)
    revArray(arr, 0, d-1)
    revArray(arr, d, n-1)
    revArray(arr, 0, n-1)

# Function to print an array
def printArray(arr):
    for i in range(0, len(arr)):
        print(arr[i])

# Driver function to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 3) # Rotate array by 3
printArray(arr)
