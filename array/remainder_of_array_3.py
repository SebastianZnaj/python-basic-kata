from functools import reduce

def remaiderAfterMultiplication(arr, n):
    result = reduce(lambda x, y: (x * y) % n, arr)
    return result

#Driver code
arr1 = [100, 10, 5, 25, 35, 14]
n1 = 11
result1 = remaiderAfterMultiplication(arr1, n1)
print(result1)

arr2 = [100, 10]
n2 = 5
result2 = remaiderAfterMultiplication(arr2, n2)
print(result2)
