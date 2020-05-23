list1 = [ [1, 2, 3],
          [4, 5, 6],
          [7, 8, 9] ]
list1 = list(reversed(list1))
print(list(zip(*list1)))
