from itertools import permutations
list2 = []
list3 = []
n = int(input("Enter the number: "))
string1 = str(n)
list1 = list(string1)
for perm in permutations(list1):
    list2.append(list(perm))
separator = ""
for i in list2:
    list3.append(int(separator.join(i)))

list3.sort()

for i in list3:
    if i > n:
        print(i, "is the next greatest number")
        break
