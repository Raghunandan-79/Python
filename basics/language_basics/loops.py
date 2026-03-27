num = int(input())

for i in range(1, 11):
    print(f"{num} x {i} = {i * num}")
print("End of for loop")


i = 1
while i <= 10:
    print(f"{num} x {i} = {i * num}")
    i += 1
print("End of while loop")

for i in range(0, 5):
    print("Hello world")
    if i == 3:
        break
else:
    print("Entire for loop was run")