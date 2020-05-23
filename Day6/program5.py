max = 1000000
fibonacci = []
a, b = 0, 1
fibonacci.append(a)
fibonacci.append(b)

sum1 = 0

while b <= max:
    temp = b + a
    if temp <= max:
        fibonacci.append(temp)
    a = b
    b = temp

list1 = list(map(int, input("Enter the space separated elements: ").split()))

for i in list1:
    if i in fibonacci:
        sum1 += i

if sum1 in fibonacci:
    print("Sum of fibonacci elements is ===> " + str(sum1) + "\nand it is a fibonacci number.")
else:
    print("Sum of fibonacci elements is ===> " + str(sum1) + "\nand it is not a fibonacci number.")
