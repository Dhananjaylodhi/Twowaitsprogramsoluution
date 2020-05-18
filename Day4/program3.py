a = int(input("Enter the no of tuples in the list: "))
b = int(input("Enter the no of elements in each tuple: "))
List1 = []
for i in range(a):
    print("Enter elements in Tuple", i + 1)
    Tuple = []
    for j in range(b):
        Tuple.append(int(input()))
    List1.append(tuple(Tuple))
N = int(input("Enter index about which you want to sort the list: "))
List1.sort(key = lambda x : x[N])
print("After sorting by Nth index sort:",List1)
