def is_monotonic(arr):
    unique_elements = set(arr)
    increasing = sorted(arr) == arr or sorted(arr, reverse=True) == arr
    return increasing

# Driver Code
arr1 = [6, 5, 4, 4]
arr2 = [5, 15, 20, 10]
arr3 = [2, 2, 2, 3]

print(is_monotonic(arr1))
print(is_monotonic(arr2))
print(is_monotonic(arr3))

