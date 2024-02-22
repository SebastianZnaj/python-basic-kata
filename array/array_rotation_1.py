# Python program of left-rotate the given array

# Function reverse the given array
# by swapping first and last numbers.

def reverse(start, end, arr):
    # No of interations needed for reversing the list
    no_of_reverse = end-start+1

    # By incrementing count value swapping
    # of first and last elements is done.
    count = 0
    while((no_of_reverse)//2 != count):
        arr[start+count], arr[end-count] = arr[end-count], arr[start+count]
        count += 1
    return arr

# Function takes array, lenght of
# array and no of rotations as input

def left_rotate_array(arr, size, d):

    # Reverse the Entire List
    start = 0
    end = size-1
    arr = reverse(start, end, arr)
    return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8]
size = 8
d = 1
print("Origin array:", arr)

# Finding all the symetric rotation number
if(d <= size):
    print("Rotated array: ", left_rotate_array(arr, size, d))
else:
    d = d % size
    print("Rotated array: ", left_rotate_array(arr, size, d))
