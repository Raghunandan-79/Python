from collections import defaultdict

dd = defaultdict(int)
dd[1] = "raj"
dd["striver"] = "raj"
dd['u'] = 99
dd["list"] = [1, 2, 3, 4]
print(dd["list"])
print(dd["xyz"])
dd["list"].append(10)
print(dd["list"])