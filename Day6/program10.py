n = int(input("Enter the no. of sorted lists: "))
final_list = []
for _ in range(n):
    list1 = list(map(int, input("Enter the space separated elements: ").split()))
    print("Given list: ", list1)
    final_list += list1
print("Final sorted list is: ", sorted(final_list))
