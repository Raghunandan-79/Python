arr = [1, 6, 2, 4]
arr.append(7)
print(arr)

arr.extend([1, 4])
print(arr)

arr.insert(1, 10)
print(arr)

arr.remove(6)
print(arr)

arr.pop()
print(arr)

arr.pop(1)
print(arr)

print(arr.index(7))

print(arr.count(1))

arr.sort()
print(arr)

arr.reverse()
print(arr)

arr2 = arr.copy()
print(arr2)

arr.clear()
print(arr)