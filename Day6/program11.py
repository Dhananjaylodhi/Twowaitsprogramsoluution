list1 = list(map(int, input("Enter the space separated elements: ").split()))
list1.sort(reverse = True)
print(list1[0] * list1[1] * list1[2], "is obtained by multiplying " 
      + str(list1[0]) + "," + str(list1[1]) + "," + str(list1[2]))
