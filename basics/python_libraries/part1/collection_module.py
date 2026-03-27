from collections import deque

# stack and queue
dq = deque([2, 3, 1])
dq.append(5)
print(dq)

dq.appendleft(7)
print(dq)

print(dq.pop())
print(dq)

print(dq.popleft())
print(dq)

dq.extend([10, 19])
print(dq)

dq.extendleft([1, 4])
print(dq)

dq.rotate(2)
print(dq)

print(len(dq))