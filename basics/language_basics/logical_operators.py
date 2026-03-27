num1, num2, num3 = map(int, input().split())

if num1 > num2 and num1 > num3:
    print("Number 1 is greatest")
elif num2 > num1 and num2 > num3:
    print("Number 2 is greatest")
else:
    print("Number 3 is greatest")

print(True or True)
print(not True)