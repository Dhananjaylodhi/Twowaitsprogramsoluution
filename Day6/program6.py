list1 = list(map(int, input("Enter the space separated elements: ").split()))
a = list1.index(min(list1))
b = list1.index(max(list1))
list2 = []
if a == 0 and b == len(list1)-1:
    print("YES, the list is only sorted but not rotated.")

else:
    for item in list1[a:]:
        list2.append(item)
    for item in list1[:b+1]:
        list2.append(item)
    if sorted(list1) == list2:
        print("YES, the list is sorted and rotated.")
    else:
        print("NO, the list is neither sorted or rotated.")
