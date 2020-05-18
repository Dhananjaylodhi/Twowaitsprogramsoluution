n = int(input("enter no. of elements: "))
list1 = []
for i in range(n):
    list1.append((input()))
tuple1 = tuple(list1)
m = input("enter element to be counted: ")
if m in tuple1:
    print(tuple1.count(m))
else:
    print("element not in tuple")
