from collections import OrderedDict

od = OrderedDict([(1, "raj"), (2, "striver"), (3, "tuf")])
print(od)
print(od[1])

if 10 in od:
    print(od[10])
else:
    print("Not in dictionary")

od.move_to_end(1)
print(od)
od.move_to_end(1, last=False)
print(od)
od[10] = "rohit"
print(od)
print(od.popitem(last=False))
print(od)
od.pop(3)
print(od)