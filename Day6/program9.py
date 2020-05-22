list1 = list(map(int, input("Enter the space separated elements: ").split()))
k = int(input("Enter the value of k: "))
if k > len(list1):
    print("Error, 'k' should be smaller than lis size.")
list1.sort()
print(list1[k-1], "is the 'kth' smallest element in the list")
