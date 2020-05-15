n = int(input("Enter Size of pattern: "))

for i in range(n):
    for j in range(n):
        if (i == j) or ((n - j -1) == i):
            print('*', end = '')
        else:
            print(' ', end = '')
    print('')
    
