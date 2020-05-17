string1 = input("enter the string: ")
string2 = ""
for i in range(len(string1)):
    if string1[i] not in string2:
        string2 += string1[i]
print("Final string: ", string2)
