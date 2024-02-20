from collections import Counter

arr = [12, 3, 4, 15]
c = Counter(arr)
sum = 0

for key, value in c.items():
    sum += key * value

print("Sum of the array is", sum)
