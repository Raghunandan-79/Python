name = "Striver"
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print("  raghu   ".strip())
name = "Raj striver"
print(name.split())

arr = ["raj", "striver"]
print("-".join(arr))

name = "raj striver raj"
print(name.replace("raj", "king"))
print(name.rfind("raj"))
print(name.index("striver"))
print(name.startswith("r"))
print(name.count("r"))
print(name.isalpha())