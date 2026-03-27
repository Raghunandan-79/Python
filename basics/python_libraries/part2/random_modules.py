import random

print(random.random())

print(random.randint(1, 10))

print(random.randrange(0, 100, 2))

print(random.choice([1, 6, 7, 8]))

print(random.sample([1, 6, 7, 8], 2))

arr = [1, 5, 6, 7]
random.shuffle(arr)
print(arr)

print(random.uniform(1.0, 10.0))