from itertools import permutations


def string_permutations(string):
    list1 = permutations(string)
    for i in list1:
        print("".join(i))


string = input("Enter the string: ")
string_permutations(string)
