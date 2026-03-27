import bisect

arr = [4, 5, 5, 6, 7, 7, 9, 10, 12, 12, 13]
arr.sort()
print(bisect.bisect_left(arr, 5))
print(bisect.bisect_right(arr, 5))
print(bisect.bisect(arr, 5))
bisect.insort(arr, 5)
print(arr)
bisect.insort_right(arr, 5)
print(arr)
bisect.insort_left(arr, 5)
print(arr)