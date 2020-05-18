votes = int(input("Enter the no of votes: "))
list1 = []
for i in range(votes):
    list1.append(input("Enter name: "))
list2 = []
for name in list1:
    list2.append((name, list1.count(name)))
list2.sort(key=lambda x: x[0], reverse=True)
list2.sort(key=lambda x: x[1])
print("Candidate who won the election: ", list2[-1][0])
