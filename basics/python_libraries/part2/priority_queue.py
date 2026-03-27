import heapq

# min heap
val = []
heapq.heappush(val, 8)
heapq.heappush(val, 3)
heapq.heappush(val, 6)
heapq.heappush(val, 1)
print(val)
heapq.heappop(val)
print(val)
heapq.heappushpop(val, 9)
print(val)
heapq.heapreplace(val, 29)
print(val)

print(heapq.nlargest(2, val))
print(heapq.nsmallest(2, val))

arr = [7, 8, 2, 1, -16, 6]
heapq.heapify(arr)
print(arr)

# max heap
arr = [6, 7, 8, 9, 10]
pq = []
for item in arr:
    heapq.heappush(pq, -1 * item)
print(-1 * pq[0])