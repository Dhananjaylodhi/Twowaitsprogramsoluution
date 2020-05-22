list1 = list(map(int, input("Enter the elements of list separated by spaces: ").split()))
list1.sort(reverse=True)
for i in range(list1[0]):
    if i not in list1:
        print(i , "is the smallest +ve no. missing from the list.")
        break
