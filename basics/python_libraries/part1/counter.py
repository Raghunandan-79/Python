from collections import Counter

arr = Counter([1, 2, 2, 3, 2, 3, 3, 4])
print(arr[3])
print(arr.most_common(3))
print(list(arr.elements()))
arr.update([7, 3])
print(list(arr.elements()))
arr.subtract([3])
print(list(arr.elements()))

c1 = Counter([1, 3, 2, 2, 2, 3, 3, 4])
c2 = Counter([3, 3, 1, 4, 5])
c3 = c1 - c2
print(list(c3.elements()))
c4 = c1 + c2
print(list(c4.elements()))
c5 = c1 & c2
print(list(c5))
c6 = c1 | c2
print(list(c6))