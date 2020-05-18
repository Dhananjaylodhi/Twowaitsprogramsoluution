dict1 = dict()
dict2 = dict()
n = int(input("Enter size of dictionary: "))
for i in range(n):
    k = input("Enter key: ")
    v = input("Enter value: ")
    dict1[k] = v
for key, value in dict1.items():
    if value not in dict2.values():
        dict2[key] = value
print("Edited dictionary: ", dict2)
