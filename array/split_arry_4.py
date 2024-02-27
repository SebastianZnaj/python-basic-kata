def split_and_add(arr, n):
    return [arr[(i + n) % len(arr)] for i in range(len(arr))]

arr = [12, 10, 5, 6, 52, 36]
n = 3

result = split_and_add(arr, n)

print(*result)
