n = int(input("enter the no. of elements: "))
l = []
for i in range(n):
    l.append(input("Enter the element: "))

for i in range(1, n - 1):
    l[i] = max(l[i + 1:])

print("result is: ", l)
