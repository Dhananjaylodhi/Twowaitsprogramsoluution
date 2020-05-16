n = int(input("Input the size of pattern: "))
for i in range(1, n):
    print("*" * (n - i) + "  " * i + "*" * (n - i))
for j in range(1, n):
    print("*" * j + "  " * (n - j) + "*" * j)
