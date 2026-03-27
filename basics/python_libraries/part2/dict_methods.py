dd = {
    1 : "raj", 
    2: "striver", 
    79: "tuf"
}

dd[100] = "century"
dd.update({10: "messi"})
print(dd.get(10))
print(dd[2])
print(dd.get(109, "not found"))
print(dd.pop(10))
dd.popitem()
print(dd)

arr = list(dd.keys())
print(arr)

arr = list(dd.values())
print(arr)

arr = list(dd.items())
print(arr)

for item in dd.items():
    print(item[0], item[1])

dd.clear()
print(dd)