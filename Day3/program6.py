def least_integer(list, n):
    result = 1
    for i in range(0, n):
        if list[i] <= result:
            result = result + list[i]
        else:
            break
    return result


n1 = int(input("Enter number of elements in list: "))
list1 = []
print("Enter elements of list: ")
for i in range(n1):
    c = int(input())
    list1.append(c)
list1.sort()
print("Smallest non-representable number: ", least_integer(list1, n1))
