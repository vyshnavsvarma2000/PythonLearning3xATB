dict = {
    "name" : "Vyshnav",
    "Age" : 24,
    "Nationality" : "Indian"
}
print(dict)
print(dict.items())
print(dict.keys())
print(dict.values())
print(dict.get("Age"))
print(dict["name"])
print(list(dict.keys()))
for i in list(dict.values()):
    print(i)
print(dict.items())
for i, j in dict.items():
    print(i, j)