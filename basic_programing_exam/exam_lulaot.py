top: int = 100
for num in range(1, top + 1):
    print(num, end=" ")
print()

num1: int = int(input("enter first number:"))
num2: int = int(input("enter second number:"))
if num1 > num2:
    num1, num2 = num2, num1
for number in range(num1, num2 + 1):
    print(number, end=" ")
print()

num: int = int(input("enter a number:"))
for number in range(0, num + 1):
    if number % 2 == 0 or number is num:
        print(number, end=" ")
print()

while True:
    den: int = int(input("enter a number:"))
    max: int = int(input("enter a number:"))
    if den > max:
        print("the first number cannot be bigger or same as the second")
        continue
    else:
        for number in range(den, max + 1):
            if number % den == 0 or number is max:
                print(number, end=" ")

    break
