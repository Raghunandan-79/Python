import math

name = "Raghu"
print(len(name))

arr = [1, 5, 6, 7, 4]
print(sorted(arr))
print(sorted(arr, reverse=True))
arr.sort()
print(arr)

arr = [-1, 5, -6, 7, 4]
print(sorted(arr, key=lambda x: abs(x)))

fruits_list = ["apple", "pineapple", "banana"]
print(sorted(fruits_list, key=len))


arr = [5, 6, 8, 7]
print(min(arr))
print(max(arr))

arr = [-15, 11, 2, 8]
print(max(arr, key=lambda x : abs(x)))

arr = [1, 2, 3, 4, 5]
print(sum(arr))
print(sum(arr, start=10))

arr = [1, 2, 3]
print(math.prod(arr))
print(len(arr))

arr = [True, False, True]
print(any(arr))
print(all(arr))

arr = [1, 6, 1, 7]
print(arr.count(1))


arr = [5, 6, 1, 3] # (index, value)
for i, val in list(enumerate(arr)):
    print(i, val)

arr = [5, 6, 1]
print(list(reversed(arr)))

arr = list(range(2, 15, 2))
print(arr)