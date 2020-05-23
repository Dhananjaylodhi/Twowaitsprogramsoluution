from itertools import permutations
list1 = list(map(float, input("Enter the space separated elements: ").split()))
list2 = []
perm = permutations(list1, 3)

for item in list(perm):
    list2.append(item)

for triplet in list2:
    if 1 < sum(triplet) < 2:
        print(triplet)
        break
        
# if no such triplet is their, then there is no output......!!
