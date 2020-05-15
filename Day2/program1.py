a = int(input("Enter the number: "))
b = a
if a % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

c = 0
for i in range(1, a + 1):
    if a % i == 0:
        c = c+1
if c == 2:
    print("number is Prime")
else:
    print("number is not Prime")

rev = 0
while b != 0:
    rem = b % 10
    rev = rev * 10 + rem
    b = b // 10
if rev == a:
    print("number is Palindrome")
else:
    print("number is not Palindrome")

e = a
sum = 0
while e != 0:
    rem2 = e % 10
    sum = sum + (rem2 * rem2 * rem2)
    e = e // 10
if sum == a:
    print("number is Armstrong number")
else:
    print("number is not Armstrong number")
