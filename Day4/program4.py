d = dict()
n = int(input("Enter size of dictionary: "))
for i in range(n):
    key = input("Enter the key: ")
    value = input("Enter thee value: ")
    d[key] = value
print("Second largest value in the dictionary is: ", list(sorted(d.values()))[-2])
